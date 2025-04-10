from django import forms

from worldOfSpeed.cars.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']

        labels = {
            'car_type': 'Type',
            'model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['car_type'].widget.attrs['placeholder'] = 'Type'
        # self.fields['model'].widget.attrs['placeholder'] = 'Model'
        # self.fields['year'].widget.attrs['placeholder'] = 'Year'
        self.fields['image_url'].widget.attrs['placeholder'] = 'https://...'
        # self.fields['price'].widget.attrs['placeholder'] = 'Price'


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']


class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.disabled = True
            field.widget.attrs['readonly'] = True

    def clean(self):
        return self.cleaned_data
