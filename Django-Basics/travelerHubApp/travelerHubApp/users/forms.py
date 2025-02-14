from django import forms

from travelerHubApp.users.models import Traveler


class TravelerBaseForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['nickname', 'email', 'country',]
        error_messages = {
            "nickname": {
                "max_length": "Your nickname is invalid!",
            }
        }

        help_texts = {
            "nickname": "*Nicknames can contain only letters and digits.",
        }


class TravelerCreateForm(TravelerBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nickname'].widget.attrs['placeholder'] = 'Enter a unique nickname...'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter a valid email address...'
        self.fields['country'].widget.attrs['placeholder'] = 'Enter a country code like <BGR>...'


class TravelerEditForm(TravelerBaseForm):
    pass


class TravelerDeleteForm(TravelerBaseForm):
    pass
