from django.urls import path

from furryFunniesApp.posts.views import PostCreateView, PostDetailView, PostEditView, PostDeleteView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('<int:pk>/details/', PostDetailView.as_view(), name='post-details'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
