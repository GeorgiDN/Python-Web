from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipediaApp.core.utils import get_profile, get_fruits
from fruitipediaApp.fruits.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipediaApp.fruits.models import Fruit


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'index.html', context)


def dashboard(request):
    profile = get_profile()
    fruits = get_fruits()
    context = {
        'profile': profile,
        'fruits': fruits
    }
    return render(request, 'dashboard.html', context)


class FruitCreateView(CreateView):
    model = Fruit
    form_class = FruitCreateForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        profile = get_profile()
        form.instance.owner = profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class FruitDetailView(DetailView):
    model = Fruit
    template_name = 'fruits/details-fruit.html'
    context_object_name = 'fruit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class FruitEditView(UpdateView):
    model = Fruit
    form_class = FruitEditForm
    template_name = 'fruits/edit-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class FruitDeleteView(DeleteView):
    model = Fruit
    form_class = FruitDeleteForm
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.get_object().__dict__

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context
