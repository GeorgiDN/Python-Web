from django.urls import path, include
from forumApp.posts import views as post_views

urlpatterns = [
    path('', post_views.index, name='index'),
    path('dashboard/', post_views.dashboard, name='dash'),
    path('add-post/', post_views.add_post, name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', post_views.delete_post, name='delete-post'),
        path('details-post/', post_views.details_page, name='details-post'),
        path('edit-post/', post_views.edit_post, name='edit-post'),
    ])),
]
