from django.shortcuts import render, redirect

from fruitipediaApp.fruits.forms import CategoryCreateForm, FruitCreateForm, FruitEditForm
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
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'fruits/create-fruit.html', context)


def details_fruit(request, fruit_id):
    fruit = Fruit.objects.get(pk=fruit_id)

    context = {
        'fruit': fruit
    }

    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, fruit_id):
    fruit = Fruit.objects.get(pk=fruit_id)

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, fruit_id):
    return render(request, 'fruits/delete-fruit.html')


def create_category(request):
    if request.method == 'GET':
        form = CategoryCreateForm()
    else:
        form = CategoryCreateForm(request.POST)

        if form.is_valid():
            form.save()
        form = CategoryCreateForm()

    context = {
        'form': form
    }

    return render(request, 'categories/create-category.html', context)
