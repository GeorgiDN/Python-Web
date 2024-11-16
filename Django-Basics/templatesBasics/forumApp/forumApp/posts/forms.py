from django import forms


class PersonForm(forms.Form):
    STATUS_CHOICE = (
        (1, "Draft"),
        (2, "Published"),
        (3, "Archived"),
    )

    person_name = forms.CharField(
        label="Person Name",
        widget=forms.TextInput(attrs={"placeholder": "Search", "class": "blue-bg"}),
        # initial="Ivan",
        max_length=10,
        error_messages={
            "required": "Please enter a value",
        },
        required=True
    )

    age = forms.IntegerField()
    is_lecturer = forms.BooleanField()

    # status = forms.IntegerField(
    #     widget=forms.Select(choices=STATUS_CHOICE)
    # )

    # status = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=STATUS_CHOICE,
    # )

    status = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=STATUS_CHOICE,
    )

