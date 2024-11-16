from django.urls import path

from forumApp import posts
from forumApp.posts.views import index, dashboard, add_post

urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dash"),
    path("add-post/", add_post, name="add-post"),
]
