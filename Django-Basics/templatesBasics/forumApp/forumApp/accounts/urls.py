from django.urls import path

from forumApp.accounts import views
from forumApp.accounts.views import UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
]
