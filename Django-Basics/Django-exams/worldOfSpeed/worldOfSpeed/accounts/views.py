from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from worldOfSpeed.accounts.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from worldOfSpeed.accounts.models import Profile
from worldOfSpeed.core.utils import get_profile, get_cars


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('catalogue')


class ProfileDetailView(View):
    template_name = 'profile/details-profile.html'

    def get(self, request, *args, **kwargs):
        profile = get_profile()
        cars = get_cars()

        context = {
            'profile': profile,
            'cars': cars,

        }

        return render(request, self.template_name, context)


class ProfileEditView(UpdateView):
    form_class = ProfileEditForm
    template_name = 'profile/profile-edit.html'

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
    template_name = 'profile/profile-delete.html'
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
