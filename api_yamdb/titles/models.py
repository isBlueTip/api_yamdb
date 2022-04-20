from django.contrib.auth import get_user_model
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


def current_year():
    return datetime.date.today().year


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
    genre = models.ManyToManyField(Genre, through="Genre_title")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Genre_title(models.Model):
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name="genre_title",
        blank=True,
        null=True,
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="genre_title",
        blank=True,
        null=True,
    )
