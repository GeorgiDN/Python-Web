from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from forumApp.posts.forms import PersonForm


def index(request):
    form = PersonForm(request.POST or None)

    if request.method == 'POST':
        print(request.POST['person_name'])

    if form.is_valid():
        print(form.cleaned_data['person_name'])

    context = {
        'my_form': form,
    }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create django project?",
                "author": "Diyan Kalaydzhiev",
                "content": "I **really** don't how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 1?",
                "author": "",
                "content": "### I really don't know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 2?",
                "author": "Diyan Kalaydzhiev",
                "content": "",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)
