from django.urls import path, include
from forumApp.posts import views as post_views

urlpatterns = [
    path('', post_views.index, name='index'),
    path('dashboard/', post_views.DashBoardView.as_view(), name='dash'),
    path('add-post/', post_views.AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', post_views.DeletePostView.as_view(), name='delete-post'),
        path('details-post/', post_views.PostDetailView.as_view(), name='details-post'),
        path('edit-post/', post_views.EditPostView.as_view(), name='edit-post'),
    ])),
]
