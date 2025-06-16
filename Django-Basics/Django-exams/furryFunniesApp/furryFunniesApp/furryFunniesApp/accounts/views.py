from django.urls import reverse_lazy
from django.views.generic import CreateView
from furryFunniesApp.accounts.models import Author
from furryFunniesApp.accounts.forms import ProfileCreateForm


class ProfileCreateView(CreateView):
    model = Author
    form_class = ProfileCreateForm
    template_name = 'accounts/create-author.html'
    success_url = reverse_lazy('dashboard')
