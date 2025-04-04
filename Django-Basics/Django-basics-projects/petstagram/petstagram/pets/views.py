from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetAddForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


def pet_add_page(request):
    form = PetAddForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profile-details", pk=1)

    context = {
        "form": form,
    }

    return render(request, "pets/pet-add-page.html", context)


def pet_edit_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)  # Fetch the pet instance using the slug

    if request.method == "POST":
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("pet-details", username=username, pet_slug=pet_slug)
    else:
        form = PetEditForm(instance=pet)  # Prepopulate form with the pet instance

    context = {
        "form": form,
        "pet": pet,
    }

    return render(request, "pets/pet-edit-page.html", context)


def pet_delete_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)

    if request.method == "POST":
        pet.delete()
        return redirect("profile-details", pk=1)

    context = {
        "form": form,
        'pet': pet
    }

    return render(request, "pets/pet-delete-page.html", context)


def pet_details_page(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()


    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
    }

    return render(request, 'pets/pet-details-page.html', context)
