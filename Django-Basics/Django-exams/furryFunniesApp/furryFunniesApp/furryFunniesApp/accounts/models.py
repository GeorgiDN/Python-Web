from django.core.validators import MinLengthValidator
from django.db import models

from furryFunniesApp.core.custom_validators import validate_letters_only, passcode_validator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(4), validate_letters_only],
    )
    last_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), validate_letters_only],
    )
    passcode = models.CharField(
        max_length=6,
        validators=[passcode_validator],
        help_text="Your passcode must be a combination of 6 digits"
    )
    pets_number = models.SmallIntegerField()
    info = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

