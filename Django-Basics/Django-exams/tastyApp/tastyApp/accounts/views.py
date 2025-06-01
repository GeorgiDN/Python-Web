from django.db.models import Sum, Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from tastyApp.accounts.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from tastyApp.accounts.models import Profile
from tastyApp.core.utils import get_recipies, get_profile
from tastyApp.recipie.models import Recipie


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('catalogue')


class ProfileDetailView(View):
    template_name = 'profile/details-profile.html'

    def get(self, request, *args, **kwargs):
        profile = get_profile()
        recipes = get_recipies()
        total_recipes = Recipie.objects.filter(author=profile).aggregate(
            total=Count('id')
        )['total']

        context = {
            'profile': profile,
            'recipes': recipes,
            'total_recipes': total_recipes,
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
            return redirect('profile-details')

        context = {'form': form, 'profile': profile}
        return render(request, self.template_name, context)


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile/delete-profile.html'
    form_class = ProfileDeleteForm
    success_url = reverse_lazy('home_page')

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
            return redirect('home_page')

        context = {'form': form, 'profile': profile}
        return render(request, self.template_name, context)
