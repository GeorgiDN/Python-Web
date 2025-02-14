from django import forms

from travelerHubApp.trip.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'summary', 'start_date', 'duration', 'image_url']
        widgets = {
            'start_date': forms.DateInput(attrs={"type": "date",}),
        }

        help_texts= {
            "duration": "*Duration in days is expected.",
        }


class TripCreateForm(TripBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['destination'].widget.attrs['placeholder'] = 'Enter a short destination note...'
        self.fields['summary'].widget.attrs['placeholder'] = 'Share your exciting moments...'
        self.fields['start_date'].widget.attrs['placeholder'] = 'Share your exciting moments...'
        self.fields['image_url'].widget.attrs['placeholder'] = 'An optional image URL...'


class TripEditForm(TripBaseForm):
    pass


class TripDeleteForm(TripBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.disabled = True  # Prevent user input
            field.widget.attrs['readonly'] = True

