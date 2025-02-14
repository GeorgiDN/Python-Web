from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from travelerHubApp.trip.forms import TripCreateForm, TripEditForm, TripDeleteForm
from travelerHubApp.trip.models import Trip
from travelerHubApp.utils.profile_utils import get_profile


def index(request):
    traveler = get_profile()
    context = {'traveler': traveler}
    return render(request, 'index.html', context)


class TripListView(ListView):
    model = Trip
    template_name = 'all-trips.html'
    context_object_name = 'trips'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_profile()
        return context


class TripCreateView(CreateView):
    model = Trip
    form_class = TripCreateForm
    template_name = 'create-trip.html'
    success_url = reverse_lazy('all-trips')

    def form_valid(self, form):
        traveler = get_profile()
        form.instance.traveler = traveler
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_profile()
        return context


class TripDetailView(DetailView):
    model = Trip
    template_name = 'details-trip.html'
    context_object_name = 'trip'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_profile()
        return context


class TripEditView(UpdateView):
    model = Trip
    form_class = TripEditForm
    template_name = 'edit-trip.html'
    success_url = reverse_lazy('all-trips')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_profile()
        return context


class TripDeleteView(DeleteView):
    model = Trip
    form_class = TripDeleteForm
    template_name = 'delete-trip.html'
    success_url = reverse_lazy('all-trips')

    def get_initial(self):
        return self.get_object().__dict__

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['traveler'] = get_profile()
        return context
