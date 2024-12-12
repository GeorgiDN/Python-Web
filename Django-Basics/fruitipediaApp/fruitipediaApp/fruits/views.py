from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from fruitipediaApp.fruits.forms import CategoryCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipediaApp.fruits.models import Fruit


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }

    return render(request, 'common/dashboard.html', context)


class CreateFruit(CreateView):
    model = Fruit
    form_class = FruitCreateForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')


# def create_fruit(request):
#     if request.method == 'GET':
#         form = FruitCreateForm()
#     else:
#         form = FruitCreateForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             return redirect('dashboard')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'fruits/create-fruit.html', context)


def details_fruit(request, fruit_id):
    fruit = Fruit.objects.get(pk=fruit_id)

    context = {
        'fruit': fruit
    }

    return render(request, 'fruits/details-fruit.html', context)


class FruitEditView(UpdateView):
    model = Fruit
    form_class = FruitEditForm
    template_name = 'fruits/edit-fruit.html'
    context_object_name = 'fruit'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        fruit_id = self.kwargs.get('fruit_id')
        return Fruit.objects.get(pk=fruit_id)

# def edit_fruit(request, fruit_id):
#     fruit = Fruit.objects.get(pk=fruit_id)
#
#     if request.method == 'GET':
#         form = FruitEditForm(instance=fruit)
#     else:
#         form = FruitEditForm(request.POST, instance=fruit)
#
#         if form.is_valid():
#             form.save()
#
#             return redirect('dashboard')
#
#     context = {
#         'form': form,
#         'fruit': fruit,
#     }
#
#     return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, fruit_id):
    fruit = Fruit.objects.get(pk=fruit_id)

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)

        if form.is_valid():
            fruit.delete()

        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/delete-fruit.html', context)


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
