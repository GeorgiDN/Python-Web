from tastyApp.accounts.models import Profile
from tastyApp.recipie.models import Recipie


def get_profile():
    return Profile.objects.first()


def get_recipies():
    return Recipie.objects.all() if Recipie.objects.all() else None
