from django import forms

from tastyApp.accounts.models import Profile


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = ('nickname', 'first_name', 'last_name', 'chef')

        labels = {
            'nickname': 'NickName',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'chef': 'Chef',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('author',)


class ProfileDeleteForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ()
