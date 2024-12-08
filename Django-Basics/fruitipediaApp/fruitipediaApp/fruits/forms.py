from django import forms

from fruitipediaApp.fruits.models import Fruit, Category


class CategoryBaseFrom(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryAddForm(CategoryBaseFrom):
    pass
