from django.urls import path, include

from forumApp.posts.views import Index, IndexView, \
    RedirectHomeView, DashboardView, AddPostView, EditPostView, DeletePostView, PostDetailView, approve_post, \
    notify_all_users

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dashboard/", DashboardView.as_view(), name="dash"),
    path("add-post/", AddPostView.as_view(), name="add-post"),
    path("notify-users/<int:post_id>/", notify_all_users, name="notify-users"),
    path("<int:pk>/", include([
        path("approve/", approve_post, name="approve"),
        path("delete-post/", DeletePostView.as_view(), name="delete-post"),
        path("details-post/", PostDetailView.as_view(), name="details-post"),
        path("edit-post/", EditPostView.as_view(), name="edit-post"),
    ])),
    path("redirect-home/", RedirectHomeView.as_view(), name="redirect-home"),
]
