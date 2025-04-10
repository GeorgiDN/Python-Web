from django.urls import path

from worldOfSpeed.cars import views

urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.CarCreateView.as_view(), name='car-create'),
    path('<int:pk>/details/', views.CarDetailView.as_view(), name='car-detail'),
    path('<int:pk>/edit/', views.CarEditView.as_view(), name='car-edit'),
    path('<int:pk>/delete/', views.CarDeleteView.as_view(), name='car-delete'),
]
