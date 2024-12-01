from django.urls import path
from albums import views

urlpatterns = [
    path("add/", views.AlbumCreateView.as_view(), name="add-album"),
]
