from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from furryFunniesApp.accounts.models import Author
from furryFunniesApp.accounts.forms import ProfileCreateForm
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
