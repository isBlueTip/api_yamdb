import uuid

from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken

from api_yamdb.settings import ADMIN_EMAIL


def send_otp(email):
    key = uuid.uuid4().hex
    send_mail(
        'Регистрация нового пользователя',
        f'Ваш код подтверждения: {key}.'
        'Используйте его для авторизации.',
        ADMIN_EMAIL,  # 'from' field
        [email],  # 'to' field
        fail_silently=False,
    )
    return key


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
    }
