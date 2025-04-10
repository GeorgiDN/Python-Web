from worldOfSpeed.accounts.models import Profile
from worldOfSpeed.cars.models import Car


def get_profile():
    return Profile.objects.first()


def get_cars():
    return Car.objects.all() if Car.objects.all() else None


def get_total_price(profile, cars):
    total_price = 0
    if profile:
        for car in cars:
            total_price += car.price
    return total_price
