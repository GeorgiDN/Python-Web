from django.db import models


class GenreChoices(models.TextChoices):
    POP = "Pop Music", "Pop Music"
    JAZZ = "Jazz Music", "Jazz Music"
    RNB = "R&B Music", "R&B Music"
    COUNTRY = "Rock Music", "Rock Music"
    ROCK = "Country Music", "Country Music"
    DANCE = "Dance Music", "Dance Music"
    HIPHOP = "Hip Hop Music", "Hip Hop Music"
    OTHER = "Other", "Other"
