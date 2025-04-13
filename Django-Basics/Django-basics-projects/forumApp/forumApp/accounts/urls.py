from django.contrib.auth.views import LoginView
from django.urls import path

from forumApp.accounts import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
