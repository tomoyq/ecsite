from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .forms import SignupForm

User = get_user_model()


class RegistView(CreateView):
    template_name = 'registration/regist.html'
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('registDone')

class RegistDoneView(TemplateView):
    template_name = 'registration/regist_done.html'