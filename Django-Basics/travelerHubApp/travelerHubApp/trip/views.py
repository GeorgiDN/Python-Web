from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from travelerHubApp.trip.forms import TripCreateForm, TripEditForm, TripDeleteForm
from travelerHubApp.trip.models import Trip


def index(request):
    return render(request, 'index.html')


class TripListView(ListView):
    model = Trip
    template_name = 'all-trips.html'
    context_object_name = 'trips'


class TripCreateView(CreateView):
    model = Trip
    form_class = TripCreateForm
    template_name = 'create-trip.html'
    success_url = reverse_lazy('index')


class TripDetailView(DetailView):
    model = Trip
    template_name = 'details-trip.html'
    context_object_name = 'trip'


class TripEditView(UpdateView):
    model = Trip
    form_class = TripEditForm
    template_name = 'edit-trip.html'
    success_url = reverse_lazy('all-trips')


class TripDeleteView(DeleteView):
    model = Trip
    form_class = TripDeleteForm
    template_name = 'delete-trip.html'
    success_url = reverse_lazy('all-trips')

# def trip_details(request, pk):
#     trip = Trip.objects.get(pk=pk)
#     context = {'trip': trip}
#     return render(request, 'details-trip.html', context)
