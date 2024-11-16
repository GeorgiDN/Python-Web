from django import forms
from forumApp.posts.choises import LanguageChoice
from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        # exclude = ["title"]

        # widgets = {
        #     "title": forms.NumberInput,
        # }

        labels = {
            "title": "Title label",
        }

        help_texts = {
            "title": "This is the title",
        }


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
        label="",
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search for post...",
            }
        )
    )



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

