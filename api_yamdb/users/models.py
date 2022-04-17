from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'


class User(AbstractUser):
    USER_ROLES = [
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
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
    role = models.CharField(max_length=32, choices=USERS_ROLES, default='user')
    confirmation_code = models.CharField(max_length=8)
