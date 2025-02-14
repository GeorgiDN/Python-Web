from django.urls import path

from travelerHubApp.users import views as profile_views

urlpatterns = [
    path('traveler/create/', profile_views.ProfileCreateView.as_view(), name='profile-create'),
    path('traveler/details/', profile_views.ProfileDetailView.as_view(), name='profile-detail'),
    path('traveler/edit/', profile_views.ProfileEditView.as_view(), name='profile-edit'),
    path('traveler/delete/', profile_views.ProfileDeleteView.as_view(), name='profile-delete'),
]
