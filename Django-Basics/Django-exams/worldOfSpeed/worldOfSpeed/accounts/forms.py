from django import forms

from worldOfSpeed.accounts.models import Profile


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        help_texts = {
            'password': "Age requirement: 21 years and above.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['age'].widget.attrs['placeholder'] = 'Age'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
