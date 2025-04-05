from django import forms
from petstagram.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={
                "placeholder": "Add a comment...",
                "rows": 4,
                "cols": 40,
                "class": "form-control",  # Add CSS class if needed
            }),
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by Pet name..."}
        ))
