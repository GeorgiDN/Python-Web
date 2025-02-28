from django.urls import path

from fruitipediaApp.accounts import views as profile_views

urlpatterns = [
    path('create/', profile_views.ProfileCreateView.as_view(), name='create-profile'),
    path('details/', profile_views.ProfileDetailView.as_view(), name='details-profile'),
    path('edit/', profile_views.ProfileEditView.as_view(), name='edit-profile'),
    path('delete/', profile_views.ProfileDeleteView.as_view(), name='delete-profile'),
]
