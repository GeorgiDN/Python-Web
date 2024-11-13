from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Hello world!</h1>")


def view_with_name(request, variable):
    return HttpResponse(f"<h1>Variable: {variable}</h1>")


def view_with_int_pk(request, pk):
    return HttpResponse(f"<h1>Int PK: {pk}</h1>")

