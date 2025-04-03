from django import forms
from django.core.exceptions import ValidationError

from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        error_messages = {
            'title': {
                'required': 'Please enter the title of your post',
                'max_length': f'The title is too long. Please keep it under {Post.TITLE_MAX_LENGTH} characters',
            },
            'author': {
                'required': 'Please enter an author'
            },
        }

    def clean_author(self):
        author = self.cleaned_data['author']

        if not author[0].isupper():
            raise ValidationError('Author name should start with uppercase letter')

        return author

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and title in content:
            raise ValidationError("The post title can not be included in post content")

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)

        post.title = post.title.capitalize()

        if commit:
            post.save()

        return post


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)


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
