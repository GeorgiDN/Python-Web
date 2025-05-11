from django.contrib import admin
from django.contrib.admin import ModelAdmin

from libraryApi2.books.models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass
