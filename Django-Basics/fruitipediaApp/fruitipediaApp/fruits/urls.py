from django.urls import path, include

from fruitipediaApp.fruits import views as fruits_views

urlpatterns = [
    path('create/', fruits_views.FruitCreateView.as_view(), name='create-fruit'),
    path('<int:pk>/details/', fruits_views.FruitDetailView.as_view(), name='details-fruit'),
    path('<int:pk>/edit/', fruits_views.FruitEditView.as_view(), name='edit-fruit'),
    path('<int:pk>/delete/', fruits_views.FruitDeleteView.as_view(), name='delete-fruit'),
]
