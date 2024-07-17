from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Item(models.Model):
    name = models.CharField(max_length = 100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Cart(models.Model):
    cart_item = models.ManyToManyField(to=CartItem, blank=True)

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    order_item = models.ManyToManyField(to=CartItem)
    order_price = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now=True)