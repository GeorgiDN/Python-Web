from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from travelerHubApp.users.forms import TravelerCreateForm, TravelerEditForm, TravelerDeleteForm
from travelerHubApp.users.models import Traveler


class ProfileCreateView(CreateView):
    model = Traveler
    form_class = TravelerCreateForm
    template_name = 'create-traveler.html'
    success_url = reverse_lazy('all-trips')


class ProfileDetailView(DetailView):
    model = Traveler
    template_name = 'details-trip.html'
    context_object_name = 'traveler'


class ProfileEditView(UpdateView):
    model = Traveler
    form_class = TravelerEditForm
    template_name = 'edit-traveler.html'
    success_url = reverse_lazy('all-trips')


class ProfileDeleteView(DeleteView):
    model = Traveler
    template_name = 'delete-traveler.html'
    form_class = TravelerDeleteForm
    success_url = reverse_lazy('all-trips')
