from django import forms
from django.core.exceptions import ValidationError

from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...',
            }
        )
    )


# EXAMPLE
# class PersonForm(forms.Form):
#     STATUS_CHOICE = (
#         ('1', 'Draft'),
#         ('2', 'Published'),
#         ('3', 'Archieved'),
#     )
#
#     person_name = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'Name'}),
#         max_length=10,
#     )
#     age = forms.IntegerField()
#
#     status = forms.IntegerField(
#         widget=forms.Select(choices=STATUS_CHOICE)
#     )
#
#     checkboxes = forms.MultipleChoiceField(
#         choices=STATUS_CHOICE,
#         widget=forms.CheckboxSelectMultiple
#     )
