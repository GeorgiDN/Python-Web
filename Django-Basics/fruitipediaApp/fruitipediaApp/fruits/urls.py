from django.urls import path

from fruitipediaApp.fruits import views as fruits_views

urlpatterns = [
    path('create/', fruits_views.FruitCreateView.as_view(), name='create-fruit'),
]
