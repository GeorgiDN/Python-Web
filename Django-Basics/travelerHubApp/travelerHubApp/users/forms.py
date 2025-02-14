from django import forms

from travelerHubApp.users.models import Traveler


class TravelerBaseForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['nickname', 'email', 'country',]


class TravelerCreateForm(TravelerBaseForm):
    pass


class TravelerEditForm(TravelerBaseForm):
    pass


class TravelerDeleteForm(TravelerBaseForm):
    pass
