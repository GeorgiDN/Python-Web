from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


class HomePageView(ListView):
    model = Photo
    template_name = "common/home-page.html"
    context_object_name = "all_photos"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')

        if pet_name:
            queryset = queryset.filter(
                tagged_pets__name__icontains=pet_name
            )

        return queryset


# def home_page(request):
#     all_photos = Photo.objects.all()
#     comment_form = CommentForm()
#     search_form = SearchForm(request.GET)
#
#     if search_form.is_valid():
#         all_photos = all_photos.filter(
#             tagged_pets__name__icontains=search_form.cleaned_data["pet_name"],
#         )
#
#     photos_per_page = 1
#     paginator = Paginator(all_photos, photos_per_page)
#     page_number = request.GET.get('page')
#
#     try:
#         all_photos = paginator.page(page_number)
#     except PageNotAnInteger:
#         all_photos = paginator.page(1)
#     except EmptyPage:
#         all_photos = paginator.page(paginator.num_pages)
#
#     context = {
#             "all_photos": all_photos,
#             "comment_form": comment_form,
#             "search_form": search_form,
#         }
#
#     return render(request, 'common/home-page.html', context)


@login_required
def likes_functionality(request, photo_id: int):
    liked_object = Like.objects.filter(
        to_photo_id=photo_id,
        user=request.user,
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo_id=photo_id, user=request.user)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


def share_functionality(request, photo_id: int):
    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))
    # HTTP_HOST = http://127.0.0.1/   + photos/<int:pk>/ => http://127.0.0.1/photos/<int:pk>/

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


@login_required
def comment_functionality(request, photo_id):
    if request.method == "POST":
        photo = Photo.objects.get(pk=photo_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META.get("HTTP_REFERER") + f"#{photo_id}")

