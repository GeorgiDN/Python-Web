from django.shortcuts import render

from tastyApp.core.utils import get_profile, get_recipies


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
