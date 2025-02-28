from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from fruitipediaApp.accounts.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from fruitipediaApp.accounts.models import Profile
from fruitipediaApp.core.utils import get_profile, get_fruits


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('dashboard')


class ProfileDetailView(View):
    template_name = 'profile/details-profile.html'

    def get(self, request, *args, **kwargs):
        profile = get_profile()
        fruits = get_fruits()
        fruits_count = len(fruits)
        context = {
            'profile': profile,
            'fruits': fruits,
            'fruits_count': fruits_count
        }
        return render(request, self.template_name, context)


class ProfileEditView(UpdateView):
    form_class = ProfileEditForm
    template_name = 'profile/edit-profile.html'

    def get(self, request, *args, **kwargs):
        profile = get_profile()
        form = self.form_class(instance=profile)
        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        profile = get_profile()
        form = self.form_class(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details-profile')

        context = {'form': form, 'profile': profile}
        return render(request, self.template_name, context)


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile/delete-profile.html'
    form_class = ProfileDeleteForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        profile = get_profile()
        form = self.form_class(instance=profile)
        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        profile = get_profile()
        form = self.form_class(request.POST, instance=profile)

        if form.is_valid():
            profile.delete()
            return redirect('index')

        context = {'form': form, 'profile': profile}
        return render(request, self.template_name, context)
