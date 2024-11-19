from datetime import datetime

from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

from forumApp.posts.forms import PostBaseForm, PostCreateForm, PostDeleteForm, SearchForm, CommentFormSet
from forumApp.posts.models import Post


def index(request):
    post_form = modelform_factory(
        Post,
        fields=("title", "content", "author", "languages"),
    )

    context = {
        "my_form": post_form,
    }

    return render(request, "posts/common/index.html", context)


def dashboard(request):
    form = SearchForm(request.GET)
    post = Post.objects.all()

    if request.method == "GET":

        if form.is_valid():
            query = form.cleaned_data["query"]
            post = post.filter(title__icontains=query)

    context = {
        "posts": post,
        "form": form,
    }

    return render(request, "posts/dashboard.html", context)


def add_post(request):
    form = PostCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("dash")

    context = {
        "form": form,
    }

    return render(request, "posts/add-post.html", context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        form = PostCreateForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect("dash")
    else:
        form = PostCreateForm(instance=post)

    context = {
        "form": form,
        "post": post,
    }

    return render(request, "posts/edit-post.html", context)


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)
    formset = CommentFormSet(request.POST or None)

    comments = post.post_comments.all()

    if request.method == "POST":
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect("details-post", pk=post.id)

    context = {
        "post": post,
        "formset": formset,
        "comments": comments,
    }

    return render(request, "posts/details-post.html", context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect("dash")

    context = {
        "form": form,
        "post": post,
    }

    return render(request, "posts/delete-post.html", context)
