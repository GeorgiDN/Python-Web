from django import forms

from tastyApp.recipie.models import Recipie


class RecipieCreateForm(forms.ModelForm):
    class Meta:
        model = Recipie
        exclude = ['author']

        labels = {
            'title': 'Title',
            'cuisine_type': 'Cuisine Type',
            'ingredients': 'Ingredients',
            'instructions': 'Instructions',
            'cooking_time': 'Cooking Time',
            'image_url': 'Image Url',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['ingredients'].widget.attrs['placeholder'] = "ingredient1, ingredient2, ..."
        self.fields['instructions'].widget.attrs['placeholder'] = "Enter detailed instructions here..."
        self.fields['image_url'].widget.attrs['placeholder'] = "Optional image URL here..."

class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipie
        exclude = ['author']


class RecipeDeleteForm(forms.ModelForm):
    class Meta:
        model = Recipie
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.disabled = True
            field.widget.attrs['readonly'] = True

    def clean(self):
        return self.cleaned_data
