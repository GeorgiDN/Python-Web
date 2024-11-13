import json

from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from urlsAndViews.departments.models import Department


def index(request):
    return HttpResponse("<h1>Hello world!</h1>")


def view_with_name(request, variable):
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request, "departments/name_template.html", {"variable": variable})


def view_with_int_pk(request, pk):
    # return HttpResponse(f"<h1>Int PK: {pk}</h1>")
    # return HttpResponse(f"<h1>Int PK: {pk}</h1>", content_type="text/plain")
    # return HttpResponse(json.dumps({"pk": pk}), content_type="application/json")
    return JsonResponse({"pk": pk})


def view_with_slug(request, pk, slug):
    # department = Department.objects.get(pk=pk, slug=slug)

    # option 1
    # department = Department.objects.filter(pk=pk, slug=slug)
    #
    # if not department:
    #     raise Http404
    # return HttpResponse(f"<h1>Department from slug: {department.first()}</h1>")

    department = get_object_or_404(Department, pk=pk, slug=slug)
    return HttpResponse(f"<h1>Department from slug: {department}</h1>")


def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect("https://softuni.bg")


def redirect_to_view(request):
    # return redirect("http://localhost:8000")
    # return redirect("home")
    return redirect("numbers", pk=2)
