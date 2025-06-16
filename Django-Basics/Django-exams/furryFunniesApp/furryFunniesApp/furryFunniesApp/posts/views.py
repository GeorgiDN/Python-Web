from django.shortcuts import render
from furryFunniesApp.core.utils import get_profile, get_posts


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'index.html', context)


def dashboard(request):
    profile = get_profile()
    posts = get_posts()

    context = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'dashboard.html', context)



