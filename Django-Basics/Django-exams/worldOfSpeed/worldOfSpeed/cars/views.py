from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from worldOfSpeed.cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
from worldOfSpeed.cars.models import Car
from worldOfSpeed.core.utils import get_profile, get_cars


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'index.html', context)


def catalogue(request):
    profile = get_profile()
    cars = get_cars()
    context = {
        'profile': profile,
        'fruits': cars
    }
    return render(request, 'catalogue.html', context)


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        profile = get_profile()
        form.instance.owner = profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car-details.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class CarEditView(UpdateView):
    model = Car
    form_class = CarEditForm
    template_name = 'cars/car-edit.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class CarDeleteView(DeleteView):
    model = Car
    form_class = CarDeleteForm
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('catalogue')

    def get_initial(self):
        return self.get_object().__dict__

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context
