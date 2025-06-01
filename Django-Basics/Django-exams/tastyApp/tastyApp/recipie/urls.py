from django.urls import path

from tastyApp.recipie import views

urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.CreateRecipeView.as_view(), name='create-recipie'),

]
