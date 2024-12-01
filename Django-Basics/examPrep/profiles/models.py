from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models

from profiles.validators import AlphaNumericValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator(),
        ]
    )

    email = models.EmailField()
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

