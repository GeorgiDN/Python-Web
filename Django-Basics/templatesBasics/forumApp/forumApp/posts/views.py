from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from forumApp.posts.forms import PersonForm


def index(request):

    form = PersonForm(request.POST or None)

    if request.method == "POST":
        print(request.POST["person_name"])

    if form.is_valid():
        print(form.cleaned_data["person_name"])

    context = {
        "my_form": form,
    }

    # print(request.POST["person_name"])

    if form.is_valid():
        pass

    return render(request, "base.html", context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create django project",
                "author": "Diyan",
                "content": "**Way** to create project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 1",
                "author": "",
                "content": "###Way to create project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 2",
                "author": "Diyan",
                "content": "",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, "posts/dashboard.html", context)
