from django import forms


class PersonForm(forms.Form):
    person_name = forms.CharField(
        max_length=10,
    )
    age = forms.IntegerField()
