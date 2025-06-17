from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from furryFunniesApp.accounts.models import Author
from furryFunniesApp.accounts.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from furryFunniesApp.core.utils import get_profile, get_posts
from furryFunniesApp.posts.models import Post


class ProfileCreateView(CreateView):
    model = Author
    form_class = ProfileCreateForm
    template_name = 'accounts/create-author.html'
    success_url = reverse_lazy('dashboard')


class ProfileDetailView(View):
    template_name = 'accounts/details-author.html'

    def get(self, request, *args, **kwargs):
        profile = get_profile()
        posts = get_posts()
        total_posts = Post.objects.filter(author=profile).aggregate(total=Count('id'))['total']
        last_updated_post = Post.objects.filter(author=profile).order_by('-updated_at').first()

        context = {
            'profile': profile,
            'posts': posts,
            'total_posts': total_posts,
            'last_updated_post': last_updated_post
        }

        return render(request, self.template_name, context)


class ProfileEditView(UpdateView):
    form_class = ProfileEditForm
    template_name = 'accounts/edit-author.html'

    def get(self, request, *args, **kwargs):
        profile = get_profile()
        form = self.form_class(instance=profile)
        context = {
            'form': form,
            'profile': profile,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        profile = get_profile()
        form = self.form_class(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile-details')

        context = {
            'form': form,
            'profile': profile
        }

        return render(request, self.template_name, context)


class ProfileDeleteView(DeleteView):
    model = Author
    template_name = 'accounts/delete-author.html'
    form_class = ProfileDeleteForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        profile = get_profile()
        form = self.form_class(instance=profile)
        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        profile = get_profile()
        form = self.form_class(request.POST, instance=profile)

        if form.is_valid():
            profile.delete()
            return redirect('index')

        context = {
            'form': form,
            'profile': profile
        }

        return render(request, self.template_name, context)
