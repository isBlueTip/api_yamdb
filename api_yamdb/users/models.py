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
    role = models.CharField(max_length=32, choices=USER_ROLES, default='user')
    confirmation_code = models.CharField(max_length=8)

    class Meta:
        ordering = ["-id"]
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username
