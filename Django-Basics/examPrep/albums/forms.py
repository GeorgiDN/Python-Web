from django import forms
from albums.models import Album
from examPrep.mixins import PlaceholderMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ("owner",)


class AlbumCreateForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumEditForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumDeleteForm(PlaceholderMixin, AlbumBaseForm):
    pass
