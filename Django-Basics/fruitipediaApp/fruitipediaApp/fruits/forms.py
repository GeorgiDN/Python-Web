from django import forms

from fruitipediaApp.fruits.models import Fruit


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['owner']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

        error_messages = {
            'fruit_name': {
                'unique': "This fruit name is already in use! Try a new one.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Fruit Name'
        self.fields['image_url'].widget.attrs['placeholder'] = 'Fruit Image URL'
        self.fields['description'].widget.attrs['placeholder'] = 'Fruit Description'
        self.fields['nutrition'].widget.attrs['placeholder'] = 'Nutrition Info'


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['owner']


class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.disabled = True
            field.widget.attrs['readonly'] = True

    def clean(self):
        return self.cleaned_data
