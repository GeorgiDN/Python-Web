from django.shortcuts import render

from fruitipediaApp.fruits.forms import CategoryAddForm
from fruitipediaApp.fruits.models import Fruit


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }

    return render(request, 'common/dashboard.html', context)


def create_fruit(request):
    return render(request, 'common/dashboard.html')


def details_fruit(request, fruit_id):
    return render(request, 'fruits/details-fruit.html')


def edit_fruit(request, fruit_id):
    return render(request, 'fruits/edit-fruit.html')


def delete_fruit(request, fruit_id):
    return render(request, 'fruits/delete-fruit.html')


def create_category(request):
    if request.method == 'GET':
        form = CategoryAddForm()
    else:
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            form.save()
            form = CategoryAddForm()

    context = {
        'form': form
    }

    return render(request, 'categories/create-category.html', context)
