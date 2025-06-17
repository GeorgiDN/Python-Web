from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furryFunniesApp.core.utils import get_profile, get_posts
from furryFunniesApp.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from furryFunniesApp.posts.models import Post


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'index.html', context)


def dashboard(request):
    profile = get_profile()
    posts = get_posts()

    context = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'dashboard.html', context)


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        profile = get_profile()
        form.instance.author = profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    context_object_name = 'post'


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.get_object().__dict__
