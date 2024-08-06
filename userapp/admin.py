from django.contrib import admin
from .models import cartModel,cartItem

# Register your models here.

admin.site.register(cartModel)
admin.site.register(cartItem)