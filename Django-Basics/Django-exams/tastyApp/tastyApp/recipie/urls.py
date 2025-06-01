from django.urls import path

from tastyApp.recipie import views

urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),]
