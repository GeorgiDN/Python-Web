from django.core.validators import MinValueValidator
from django.db import models

from musicApp.albums.choises import GenreChoices
from musicApp.profiles.models import Profile


class Album(models.Model):
    name = models.CharField(
        unique=True,
        max_length=30
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=GenreChoices.choices,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ],
    )

    owner = models.ForeignKey(
        to="profiles.Profile",
        on_delete=models.CASCADE,
        related_name="owner_albums",
    )
