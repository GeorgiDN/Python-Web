from django.urls import path

from libraryApi.books import views

urlpatterns = [
    path('books/', views.list_books_view, name='books_list'),
]
