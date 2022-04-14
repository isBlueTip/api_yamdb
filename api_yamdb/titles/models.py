from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Categories(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)


class Titles(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.CharField(max_length=200)
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name="titles",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Genre_title(models.Model):
    genre = models.ForeignKey(
        Genres,
        on_delete=models.CASCADE,
        related_name="genre_title",
        blank=True,
        null=True,
    )
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name="genre_title",
        blank=True,
        null=True,
    )
