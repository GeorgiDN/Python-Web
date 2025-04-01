from django import forms


class PersonForm(forms.Form):
    STATUS_CHOICE = (
        ('1', 'Draft'),
        ('2', 'Published'),
        ('3', 'Archieved'),
    )

    person_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
        max_length=10,
    )
    age = forms.IntegerField()

    status = forms.IntegerField(
        widget=forms.Select(choices=STATUS_CHOICE)
    )

    checkboxes = forms.MultipleChoiceField(
        choices=STATUS_CHOICE,
        widget=forms.CheckboxSelectMultiple
    )
