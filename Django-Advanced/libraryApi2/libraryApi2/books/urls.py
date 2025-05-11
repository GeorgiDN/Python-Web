from django.urls import path

from libraryApi2.books import views

urlpatterns = [
    path('', views.ListBooksView.as_view(), name='index'),
]
