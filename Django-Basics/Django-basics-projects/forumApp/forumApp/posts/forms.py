from django import forms

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
    )

    content = forms.CharField(
        widget=forms.Textarea,
    )

    author = forms.CharField(
        max_length=30,
    )

    created_at = forms.DateTimeField()

    languages = forms.ChoiceField(
        choices=LanguageChoice.choices
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
