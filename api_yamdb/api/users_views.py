import logging

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from loggers import logger, formatter
from users.models import User
from .permissions import IsAdmin
from .users_serializers import (SignupSerializer,
                                TokenSerializer,
                                UserSerializer)

from .utils import send_otp, get_tokens_for_user


LOG_NAME = 'users_views.log'

file_handler = logging.FileHandler(LOG_NAME)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class SignupView(APIView):
    """View to register a new user and verify email."""

    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get('email')
        otp = send_otp(email)
        serializer.save(confirmation_code=otp)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenView(APIView):
    """View to request a new user's JWT token."""

    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User,
                                 username=request.data.get('username'))
        token = get_tokens_for_user(user)
        return Response(token, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):
    """Viewset to work with users."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('username',)
    permission_classes = [IsAdmin, ]
    lookup_field = 'username'

    @action(detail=False,
            methods=['patch', 'get'],
            permission_classes=[IsAuthenticated],
            url_path='me',
            name='Change current user details')
    def change_user_info(self, request):
        user = self.request.user
        if request.method == 'PATCH':
            # copy request.data dict
            data = request.data.copy()
            if data.get('role'):
                data.pop('role')
            print(request.data.get('role'))
            # 'role' key from request.data only if current user is admin
            if request.user.role == 'admin' and request.data.get('role'):
                data['role'] = request.data['role']
            else:  # 'role' key = old role
                data['role'] = request.user.role
            serializer = UserSerializer(user, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
