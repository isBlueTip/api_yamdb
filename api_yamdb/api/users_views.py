import logging
from random import randint

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from .permissions import IsAdmin, IsModer
from .users_serializers import (SignupSerializer,
                                TokenSerializer,
                                UserSerializer)

from loggers import logger, formatter

LOG_NAME = 'users_views.log'

file_handler = logging.FileHandler(LOG_NAME)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)  # logger.debug(<отслеживаемый объект>)


def send_otp(email):
    key = randint(99999, 999999)
    send_mail(
        'Регистрация нового пользователя',
        f'Ваш код подтверждения: {key}.'
        'Используйте его для авторизации.',
        'yamdb@example.com',  # 'from' field
        [f'{email}'],  # 'to' field
        fail_silently=False,
    )
    return key


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        # 'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class SignupView(APIView):
    """View to register a new user and verify email."""

    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data.get('email')
            otp = send_otp(email)
            serializer.save(confirmation_code=otp)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenView(APIView):
    """View to request a new user's JWT token."""

    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User,
                                     username=request.data.get('username'))
            token = get_tokens_for_user(user)
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('username',)
    permission_classes = [IsAdmin, ]
