from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from travelerHubApp.users.validators import validate_nickname


class Traveler(models.Model):
    nickname = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            MinLengthValidator(3),
            validate_nickname
        ],
        help_text='*Nicknames can contain only letters and digits.'
    )
    email = models.EmailField(
        unique=True,
        max_length=30,
    )
    country = models.CharField(
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{3}',
            )]
    )
    about_me = models.TextField(
        null=True,
        blank=True,
    )
