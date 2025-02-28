from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaApp.core.custom_validators import validate_first_letter


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2, message="First name must be at least 2 characters long."),
            validate_first_letter
        ],
    )
    last_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(1, message="Last name must be at least 1 characters long."),
            validate_first_letter
        ],
    )
    email = models.EmailField(
        unique=True,
        max_length=40,
    )
    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8, message="Password must be at least 8 characters long."),
        ],
        help_text="*Password length requirements: 8 to 20 characters",
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
