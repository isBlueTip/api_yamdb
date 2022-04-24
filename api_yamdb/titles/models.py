from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from titles.utils import current_year

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField(
        default=current_year(),
        validators=[MinValueValidator(1984), max_value_current_year],
    )
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="titles",
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(Genre)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name
