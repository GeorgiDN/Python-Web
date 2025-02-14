from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from travelerHubApp.users.forms import TravelerCreateForm, TravelerEditForm, TravelerDeleteForm
from travelerHubApp.users.models import Traveler
from travelerHubApp.utils.profile_utils import get_profile


class ProfileCreateView(CreateView):
    model = Traveler
    form_class = TravelerCreateForm
    template_name = 'create-traveler.html'
    success_url = reverse_lazy('all-trips')



class ProfileDetailView(View):
    template_name = 'details-trip.html'

    def get(self, request, *args, **kwargs):
        traveler = get_profile() # or based on another logic you need
        context = {'traveler': traveler}
        return render(request, self.template_name, context)


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
