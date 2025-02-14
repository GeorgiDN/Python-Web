from django.urls import path

from travelerHubApp.users import views as profile_views

urlpatterns = [
    path('create/', profile_views.ProfileCreateView.as_view(), name='profile-create'),
    path('details/', profile_views.ProfileDetailView.as_view(), name='profile-details'),
    path('edit/', profile_views.ProfileEditView.as_view(), name='profile-edit'),
    path('delete/', profile_views.ProfileDeleteView.as_view(), name='profile-delete'),
]
