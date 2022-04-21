import logging

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework import status, viewsets, filters
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from users.models import User
from .permissions import IsAdmin
from .users_serializers import (SignupSerializer,
                                TokenSerializer,
                                UserSerializer,
                                MeSerializer)
from .utils import send_otp, get_tokens_for_user

from loggers import logger, formatter

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

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('username',)
    permission_classes = [IsAdmin, ]
    lookup_field = 'username'


class MeView(RetrieveUpdateAPIView):

    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all()
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user
