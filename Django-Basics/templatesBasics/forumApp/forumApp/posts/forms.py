from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forumApp.posts.choises import LanguageChoice
from forumApp.posts.mixins import DisabledFieldsMixin
from forumApp.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        error_messages = {
            "title": {
                "required": "This field is required.",
                "max_length": f"This field is too long. Max length is {Post.TITLE_MAX_LENGTH}.",
            },
            "author": {
                "required": "Please enter the author name.",
            }
        }

    def clean_author(self):
        author = self.cleaned_data.get("author")

        if not author[0].isupper():
            raise ValidationError("Author name must start with a capital letter!")
        return author

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title and content and title in content:
            raise ValidationError("The post title cannot be included in the post content")

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)

        post.title = post.title.capitalize()

        if commit:
            post.save()

        return post


        # exclude = ["title"]

        # widgets = {
        #     "title": forms.NumberInput,
        # }

        # labels = {
        #     "title": "Title label",
        # }
        #
        # help_texts = {
        #     "title": "This is the title",
        # }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisabledFieldsMixin):
    disabled_fields = ("__all__", )


class SearchForm(forms.Form):
    query = forms.CharField(
        label="",
        required=False,
        # required=True,
        # error_messages={
        #     "required": "please write something",
        #     "max_length": "Max length is 10",
        # },
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search for post...",
            }
        )
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'get'
    #     self.helper.form_class = 'form-inline'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "content")

        labels = {
            "author": "",
            "label": "",
        }

        error_messages = {
            "author": {
                "required": "Author name is required. Write it!",
            },
            "content": {
                "required": "Content is required. Write it!",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["author"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Your name",
        })

        self.fields["content"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Add message...",
            "rows": 1,
        })


CommentFormSet = formset_factory(CommentForm, extra=1)






# #######################################################################
# class PostForm(forms.ModelForm):
#     title = forms.CharField(
#         max_length=100,
#     )
#     content = forms.CharField(
#         widget=forms.Textarea,
#     )
#     author = forms.CharField(
#         max_length=30,
#     )
#     created_at = forms.DateField()
#     languages = forms.ChoiceField(
#         choices=LanguageChoice.choices,
#     )





# class PersonForm(forms.Form):
#     STATUS_CHOICE = (
#         (1, "Draft"),
#         (2, "Published"),
#         (3, "Archived"),
#     )
#
#     person_name = forms.CharField(
#         label="Person Name",
#         widget=forms.TextInput(attrs={"placeholder": "Search", "class": "blue-bg"}),
#         # initial="Ivan",
#         max_length=10,
#         error_messages={
#             "required": "Please enter a value",
#         },
#         required=True
#     )
#
#     age = forms.IntegerField()
#     is_lecturer = forms.BooleanField()
#
#     # status = forms.IntegerField(
#     #     widget=forms.Select(choices=STATUS_CHOICE)
#     # )
#
#     # status = forms.ChoiceField(
#     #     widget=forms.RadioSelect,
#     #     choices=STATUS_CHOICE,
#     # )
#
#     status = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         choices=STATUS_CHOICE,
#     )

