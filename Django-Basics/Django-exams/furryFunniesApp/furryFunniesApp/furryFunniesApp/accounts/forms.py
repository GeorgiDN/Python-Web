from django import forms
from django.forms import PasswordInput

from furryFunniesApp.accounts.models import Author


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Author

        fields = ('first_name', 'last_name', 'passcode', 'pets_number')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'passcode': 'Passcode',
            'pets_number': 'Pets Number',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = "Enter your first name..."
        self.fields['last_name'].widget.attrs['placeholder'] = "Enter your last name..."
        self.fields['passcode'].widget = PasswordInput()
        self.fields['passcode'].widget.attrs['placeholder'] = "Enter 6 digits..."
        self.fields['pets_number'].widget.attrs['placeholder'] = "Enter the number of your pets..."


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ('passcode',)
