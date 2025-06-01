from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from tastyApp.core.utils import get_profile, get_recipies
from tastyApp.recipie.forms import RecipieCreateForm, RecipeEditForm
from tastyApp.recipie.models import Recipie


def home_page(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'home-page.html', context)


def catalogue(request):
    profile = get_profile()
    recipies = get_recipies()
    recipies_number = len(recipies) if recipies else 0
    context = {
        'profile': profile,
        'recipies': recipies,
        'recipies_number': recipies_number,
    }
    return render(request, 'catalogue.html', context)


class CreateRecipeView(CreateView):
    model = Recipie
    form_class = RecipieCreateForm
    template_name = 'recipies/create-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        profile = get_profile()
        form.instance.author = profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class RecipieDetailView(DetailView):
    model = Recipie
    template_name = 'recipies/details-recipe.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class RecipeEditView(UpdateView):
    model = Recipie
    form_class = RecipeEditForm
    template_name = 'recipies/edit-recipe.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context
