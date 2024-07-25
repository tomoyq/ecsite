from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView, View

from .models import Item, CartItem, Order

User = get_user_model()

class OnlyYouMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return (user.id == self.kwargs['pk']) or (user.is_superuser)

class HomeView(ListView):
    template_name = 'core/home.html'
    model = Item

class DetailView(DetailView):
    template_name = 'core/detail.html'
    model = Item

    def get_success_url(self):
        user_pk = self.request.user.id
        return reverse_lazy('cart', kwargs={'pk': user_pk})

    def post(self, *args, **kwargs):
        item_pk = self.request.POST.get('item_pk')
        quantity = int(self.request.POST.get('quantity'))
        item = Item.objects.get(id=item_pk)
        cart_item = CartItem(item=item, quantity=quantity)
        user = self.request.user
        user.cart.add_cart_item(cart_item)
        return redirect(self.get_success_url())

class CartView(LoginRequiredMixin, OnlyYouMixin, DetailView):
    template_name = 'core/cart.html'
    model = User 
    context_object_name = 'cart'

    def get_object(self, queryset=None):
        user = super().get_object(queryset)
        return user.cart

class OrderView(View):
    def post(self, *args, **kwargs):
        order_user = self.request.user
        order_cart = order_user.cart
        order_obj = Order.objects.create(
            user = order_user,
            order_price = order_cart.total_price,
        )
        for cart_item in order_cart.cart_item.all():
            order_obj.order_item.add(cart_item)
        order_cart.cart_item.clear()

        return redirect(reverse_lazy('success'))

class SuccessView(TemplateView):
    template_name = 'core/success.html'