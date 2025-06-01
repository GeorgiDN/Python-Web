from django.core.validators import MinLengthValidator
from django.db import models

from tastyApp.accounts.models import Profile


class Recipie(models.Model):
    CUISINE_CHOICES = [
        ('French', 'French'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Balkan', 'Balkan'),
        ('Other', 'Other'),
    ]

    title = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(10)],
        error_messages={
            'unique': "We already have a recipe with the same title!",
        }
    )
    cuisine_type = models.CharField(
        max_length=20,
        choices=CUISINE_CHOICES,
        default='Other',
    )
    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space."
    )
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(
        help_text="Provide the cooking time in minutes."
    )
    image_url = models.URLField(null=True, blank=True)
    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='profile_recipies',
    )

    def __str__(self):
        return self.title
