from django.contrib import admin

from djangoIntroduction.todo_app.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
