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

    author = models.CharField(
        max_length=100
    )

    # author = models.ManyToManyField(
    #     to='Author',
    #     related_name='books',
    # )

    def __str__(self):
        return self.title
