from django.db.models import Sum, Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from tastyApp.accounts.forms import ProfileCreateForm
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
