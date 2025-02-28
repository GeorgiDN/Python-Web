from django.urls import reverse_lazy
from django.views.generic import CreateView

from fruitipediaApp.accounts.forms import ProfileCreateForm
from fruitipediaApp.accounts.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('dashboard')
