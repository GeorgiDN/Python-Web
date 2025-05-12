from django.contrib import admin
from unfold.admin import ModelAdmin

from libraryApi2.books.models import Book


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass
