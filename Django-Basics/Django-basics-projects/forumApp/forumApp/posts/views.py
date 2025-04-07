from datetime import datetime

from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView, DetailView

from forumApp.posts.forms import PostBaseForm, PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet
from forumApp.posts.models import Post


def index(request):

    context = {
        'my_form': '',
    }

    return render(request, 'common/index.html', context)


class DashBoardView(ListView, FormView):
    model = Post
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    form_class = SearchForm
    success_url = reverse_lazy('dash')

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'query' in self.request.GET:
            query = self.request.GET['query']
            queryset = queryset.filter(title__icontains=query)

        return queryset


# def dashboard(request):
#     form = SearchForm(request.GET)
#     posts = Post.objects.all()
#
#     if request.method == "GET":
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             posts = posts.filter(title__icontains=query)
#
#     context = {
#         "posts": posts,
#         "form": form,
#     }
#
#     return render(request, 'posts/dashboard.html', context)


class AddPostView(CreateView):
    model = Post
    template_name = 'posts/add_post.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('dash')


# def add_post(request):
#     form = PostCreateForm(request.POST or None, request.FILES or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('dash')
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'posts/add_post.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['formset'] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset.forms:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()
            return redirect('details-post', pk=post.id)

        context = self.get_context_data()
        context['formset'] = formset
        return self.render_to_response(context)


# def details_page(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     formset = CommentFormSet(request.POST or None)
#     comments = post.comments.all()
#
#     if request.method == "POST":
#         if formset.is_valid():
#             for form in formset:
#                 if form.cleaned_data:
#                     comment = form.save(commit=False)
#                     comment.post = post
#                     comment.save()
#
#             return redirect('details-post', pk=post.id)
#
#     context = {
#         "post": post,
#         "formset": formset,
#         "comments": comments,
#     }
#
#     return render(request, 'posts/details-post.html', context)


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dash')
    form_class = PostEditForm

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=("title", "content", "author", "languages", "image"))
        else:
            return modelform_factory(Post, fields=("content",))

# def edit_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#
#     if request.method == "POST":
#         form = PostCreateForm(request.POST, request.FILES, instance=post)
#
#         if form.is_valid():
#             form.save()
#             return redirect("dash")
#     else:
#         form = PostCreateForm(instance=post)
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#
#     return render(request, "posts/edit-post.html", context)


class DeletePostView(DeleteView, UpdateView):
    model = Post
    template_name = "posts/delete-post.html"
    success_url = reverse_lazy("dash")
    form_class = PostDeleteForm

    # def get_initial(self):
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     post = Post.objects.get(pk=pk)
    #     return post.__dict__


# def delete_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     form = PostDeleteForm(instance=post)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('dash')
#
#     context = {
#         'form': form,
#         'post': post,
#     }
#
#     return render(request, 'posts/delete-post.html', context)

