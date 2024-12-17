from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=30,
    )

    pages = models.IntegerField()

    description = models.TextField(
        max_length=100,
        default=''
    )

    author = models.ManyToManyField(
        to='Author',
        related_name='books',
    )

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name
