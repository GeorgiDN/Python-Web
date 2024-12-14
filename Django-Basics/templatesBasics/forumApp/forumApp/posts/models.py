from django.db import models

from forumApp.posts.choises import LanguageChoice
from forumApp.posts.validators import BadLanguageValidator


class Post(models.Model):
    TITLE_MAX_LENGTH = 10

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )

    content = models.TextField(
        validators=(
            BadLanguageValidator(),
        )
    )

    author = models.CharField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    approved = models.BooleanField(
        default=False,
    )

    languages = models.CharField(
        max_length=20,
        choices=LanguageChoice.choices,
        default=LanguageChoice.OTHER,
    )

    image = models.ImageField(
        upload_to="post_images/",
        blank=True,
        null=True,
    )

    class Meta:
        permissions = [
            ("can_approve_posts", "Can approve posts"),
        ]

class Comment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="post_comments",
    )
    author = models.CharField(
        max_length=100,
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
