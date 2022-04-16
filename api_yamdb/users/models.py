from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'US'
    MODER = 'MOD'
    ADMIN = 'ADM'
    USERS_ROLES = [
        (USER, 'User'),
        (MODER, 'Moderator'),
        (ADMIN, 'Admin'),
    ]
    email = models.EmailField(
        'email address',
        unique=True,
        blank=False,
        null=False,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(max_length=32, choices=USERS_ROLES, default='User')
    confirmation_code = models.CharField(max_length=8)
