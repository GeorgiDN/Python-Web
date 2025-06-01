from django.urls import path

from tastyApp.recipie import views

urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.CreateRecipeView.as_view(), name='create-recipie'),
    path('<int:pk>/details/', views.RecipieDetailView.as_view(), name='recipe-detail'),
    path('<int:pk>/edit/', views.RecipeEditView.as_view(), name='recipe-edit'),

]
