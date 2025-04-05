from django.shortcuts import render

from petstagram.photos.models import Photo


def photo_add_page(request):
    return render(request, 'photos/photo-add-page.html')


def photo_edit_page(request, pk: int):
    return render(request, 'photos/photo-edit-page.html')


def photo_details_page(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.photo_likes.all()
    comments = photo.photo_comments.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }

    return render(request, 'photos/photo-details-page.html', context)
