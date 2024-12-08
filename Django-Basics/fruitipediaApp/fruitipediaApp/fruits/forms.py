from django import forms

from fruitipediaApp.fruits.models import Fruit, Category


class CategoryBaseFrom(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryCreateForm(CategoryBaseFrom):
    pass


class FruitBaseFrom(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitCreateForm(FruitBaseFrom):
    pass


class FruitEditForm(FruitBaseFrom):
    pass


class FruitDeleteForm(FruitBaseFrom):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
