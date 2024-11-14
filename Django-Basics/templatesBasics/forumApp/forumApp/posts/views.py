from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "current_time": datetime.now(),
        "person": {
            "age": 25,
            "height": 190,
        },
        "ids": ["1234", "asd456", "qwe789"],
        "some_text": "hello my name is Diyan, and I am developer",
        "users": [
            "pesho",
            "ivan",
            "stamat",
            "maria",
            "magdalena",
        ]
    }

    return render(request, "base.html", context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create django project",
                "author": "Diyan",
                "content": "Way to create project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 1",
                "author": "",
                "content": "Way to create project",
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
