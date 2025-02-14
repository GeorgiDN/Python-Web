from travelerHubApp.users.models import Traveler


def get_profile():
    return Traveler.objects.first()
