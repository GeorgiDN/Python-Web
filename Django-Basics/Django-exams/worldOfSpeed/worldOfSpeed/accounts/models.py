from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from worldOfSpeed.core.custom_validators import validate_username


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, message="Username must be at least 3 chars long!"),
            validate_username
        ],
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=[
            MinValueValidator(21),
        ],
        help_text="Age requirement: 21 years and above."
    )
    password = models.CharField(
        max_length=20,
    )
    first_name = models.CharField(
        max_length=25,
    )
    last_name = models.CharField(
        max_length=25,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return f'{self.first_name}'
        if self.last_name:
            return f'{self.last_name}'
        return None

    def __str__(self):
        return self.username
