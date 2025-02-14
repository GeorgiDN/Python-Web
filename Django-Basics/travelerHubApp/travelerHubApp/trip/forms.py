from django import forms

from travelerHubApp.trip.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'summary', 'start_date', 'duration', 'image_url']


class TripCreateForm(TripBaseForm):
    pass


class TripEditForm(TripBaseForm):
    pass


class TripDeleteForm(TripBaseForm):
    pass
