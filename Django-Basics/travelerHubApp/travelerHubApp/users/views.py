from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from travelerHubApp.users.forms import TravelerCreateForm, TravelerEditForm, TravelerDeleteForm
from travelerHubApp.users.models import Traveler
from travelerHubApp.utils.profile_utils import get_profile, get_all_trips


class ProfileCreateView(CreateView):
    model = Traveler
    form_class = TravelerCreateForm
    template_name = 'create-traveler.html'
    success_url = reverse_lazy('all-trips')


class ProfileDetailView(View):
    template_name = 'details-traveler.html'

    def get(self, request, *args, **kwargs):
        traveler = get_profile()
        trips = get_all_trips()
        context = {
            'traveler': traveler,
            'trips': trips
        }
        return render(request, self.template_name, context)


class ProfileEditView(UpdateView):
    form_class = TravelerEditForm
    template_name = 'edit-traveler.html'

    def get(self, request, *args, **kwargs):
        traveler = get_profile()
        form = self.form_class(instance=traveler)
        context = {
            'form': form,
            'traveler': traveler,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        traveler = get_profile()
        form = self.form_class(request.POST, instance=traveler)

        if form.is_valid():
            form.save()
            return redirect('all-trips')

        context = {'form': form, 'traveler': traveler}
        return render(request, self.template_name, context)


class ProfileDeleteView(DeleteView):
    model = Traveler
    template_name = 'delete-traveler.html'
    form_class = TravelerDeleteForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        traveler = get_profile()
        form = self.form_class(instance=traveler)
        context = {
            'form': form,
            'traveler': traveler,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        traveler = get_profile()
        form = self.form_class(request.POST, instance=traveler)

        if form.is_valid():
            traveler.delete()
            return redirect('index')

        context = {'form': form, 'traveler': traveler}
        return render(request, self.template_name, context)
