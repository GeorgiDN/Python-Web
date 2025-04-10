from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from worldOfSpeed.accounts.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from worldOfSpeed.accounts.models import Profile
from worldOfSpeed.cars.models import Car
from worldOfSpeed.core.utils import get_profile, get_cars, get_total_price


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('catalogue')


class ProfileDetailView(View):
    template_name = 'profile/profile-details.html'

    def get(self, request, *args, **kwargs):
        profile = get_profile()
        cars = get_cars()
        # total_sum = get_total_price(profile, cars)
        total_sum = Car.objects.filter(owner=profile, owner__isnull=False) \
                          .aggregate(total_price=Sum('price'))['total_price'] or 0

        context = {
            'profile': profile,
            'cars': cars,
            'total_sum': total_sum,
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
            return redirect('profile-details')

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
