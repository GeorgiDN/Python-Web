from fruitipediaApp.accounts.models import Profile
from fruitipediaApp.fruits.models import Fruit


def get_profile():
    return Profile.objects.first()


def get_fruits():
    return Fruit.objects.all() if Fruit.objects.all() else None
