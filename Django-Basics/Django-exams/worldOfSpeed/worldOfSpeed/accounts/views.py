from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from worldOfSpeed.accounts.forms import ProfileCreateForm
from worldOfSpeed.accounts.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('catalogue')

