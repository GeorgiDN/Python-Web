from django.urls import path

from furryFunniesApp.posts.views import PostCreateView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create-post'),
]
