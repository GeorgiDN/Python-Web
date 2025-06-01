from django.urls import reverse_lazy
from django.views.generic import CreateView

from tastyApp.accounts.forms import ProfileCreateForm
from tastyApp.accounts.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('catalogue')
