from django.urls import path
from todoApp.todos.views import TodoListCreateApiView, CategoriesListView

urlpatterns = [
    path('', TodoListCreateApiView.as_view(), name='todo-list-create'),
    path('categories/', CategoriesListView.as_view(), name='category-list'),
]
