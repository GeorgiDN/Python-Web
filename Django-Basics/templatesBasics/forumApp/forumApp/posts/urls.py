from django.urls import path, include

from forumApp.posts.views import Index, delete_post, details_page, IndexView, \
    RedirectHomeView, DashboardView, AddPostView, EditPostView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("dashboard/", DashboardView.as_view(), name="dash"),
    path("add-post/", AddPostView.as_view(), name="add-post"),
    path("<int:pk>/", include([
        path("delete-post/", delete_post, name="delete-post"),
        path("details-post/", details_page, name="details-post"),
        path("edit-post/", EditPostView.as_view(), name="edit-post"),
    ])),
    path("redirect-home/", RedirectHomeView.as_view(), name="redirect-home"),
]
