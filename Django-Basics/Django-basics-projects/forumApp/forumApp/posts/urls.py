from django.urls import path
from forumApp.posts import views as post_views

urlpatterns = [
    path('', post_views.index, name='index'),
    path('dashboard/', post_views.dashboard, name='dash'),
    path('add-post/', post_views.add_post, name='add-post'),
]
