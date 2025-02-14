from django.urls import path

from travelerHubApp.trip import views as trip_views

urlpatterns = [
    path('', trip_views.index, name='index'),
    path('all-trips', trip_views.TripListView.as_view(), name='all-trips'),
    path('trips/create', trip_views.TripCreateView.as_view(), name='create-trip'),
    path('trips/<int:pk>/details', trip_views.TripDetailView.as_view(), name='trip-details'),
    path('trips/<int:pk>/edit', trip_views.TripEditView.as_view(), name='trip-edit'),
    path('trips/<int:pk>/delete', trip_views.TripDeleteView.as_view(), name='trip-delete'),
]
