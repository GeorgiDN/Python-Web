from django.urls import path
from todoApp.accounts.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

]
