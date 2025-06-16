from django import forms

from furryFunniesApp.posts.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']

        labels = {
            'title': 'Title',
            'image': 'Post Image URL:',
            'content': 'Content:',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = "Put an attractive and unique title..."
        self.fields['image'].widget.attrs['placeholder'] = "Share your funniest furry photo URL!"
        self.fields['content'].widget.attrs['placeholder'] = "Share some interesting facts about your adorable pets..."


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']
