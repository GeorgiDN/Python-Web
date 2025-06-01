from django.contrib import admin

from tastyApp.accounts.models import Profile
from tastyApp.recipie.models import Recipie


@admin.register(Recipie)
class RecipieAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
