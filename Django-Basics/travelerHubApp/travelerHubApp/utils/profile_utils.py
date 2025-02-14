from travelerHubApp.trip.models import Trip
from travelerHubApp.users.models import Traveler


def get_profile():
    return Traveler.objects.first()


def get_all_trips():
    return Trip.objects.all().order_by('-start_date') or None
