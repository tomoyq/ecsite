from django.contrib import admin

from .models import *

admin.site.register(Item)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)
