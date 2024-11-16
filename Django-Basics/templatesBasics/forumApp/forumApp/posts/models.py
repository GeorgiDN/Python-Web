from django.db import models

from forumApp.posts.choises import LanguageChoice


class Post(models.Model):
    TITLE_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    content = models.TextField()
    author = models.CharField(
        max_length=30,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    languages = models.CharField(
        max_length=20,
        choices=LanguageChoice.choices,
        default=LanguageChoice.OTHER,
    )
