from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('cart/<int:pk>', CartView.as_view(), name='cart'),
    path('order/', OrderView.as_view(), name='order'),
    path('success/', SuccessView.as_view(), name='success'),
]