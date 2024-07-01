from django.urls import reverse_lazy

from django.views.generic.base import TemplateView, RedirectView

class HomeView(TemplateView):
    template_name = 'core/home.html'

class DetailView(TemplateView):
    template_name = 'core/detail.html'

class CartView(TemplateView):
    template_name = 'core/cart.html'

class OrderView(RedirectView):
    url = reverse_lazy('success')

class SuccessView(TemplateView):
    template_name = 'core/success.html'