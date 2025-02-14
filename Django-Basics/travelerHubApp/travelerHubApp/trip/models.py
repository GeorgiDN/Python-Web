from django.core.validators import MinLengthValidator
from django.db import models

from travelerHubApp.users.models import Traveler


class Trip(models.Model):
    destination = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3),
        ]
    )
    summary = models.TextField()
    start_date = models.DateField()
    duration = models.PositiveSmallIntegerField(
        default=1,
        help_text='*Duration in days is expected.'
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    traveler = models.ForeignKey(
        to=Traveler,
        on_delete=models.CASCADE,
        related_name='trips',
    )

    class Meta:
        ordering = ['-start_date']
