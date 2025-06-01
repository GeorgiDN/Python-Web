from django.core.validators import MinLengthValidator
from django.db import models

from tastyApp.core.custom_validators import validate_capitalized


class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(
                2,
                message="Nickname must be at least 2 chars long!")]
    )
    first_name = models.CharField(
        max_length=30,
        validators=[validate_capitalized],
    )
    last_name = models.CharField(
        max_length=30,
        validators=[validate_capitalized],
    )
    chef = models.BooleanField(default=False)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nickname
