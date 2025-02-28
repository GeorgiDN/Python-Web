from django.urls import path

from fruitipediaApp.accounts import views as profile_views

urlpatterns = [
    path('create/', profile_views.ProfileCreateView.as_view(), name='create-profile'),
]
