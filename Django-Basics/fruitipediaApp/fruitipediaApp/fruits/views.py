from django.shortcuts import render

from fruitipediaApp.core.utils import get_profile, get_fruits


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
