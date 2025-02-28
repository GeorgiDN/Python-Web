from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaApp.accounts.models import Profile
from fruitipediaApp.core.custom_validators import validate_letters


class Fruit(models.Model):
    name = models.CharField(
        unique=True,
        max_length=30,
        validators=[
            MinLengthValidator(2, message='Name must be between 2 and 30 characters'),
            validate_letters
        ],
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.'
        }
    )
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='fruits',
    )

    def __str__(self):
        return f'Fruit {self.name}'
