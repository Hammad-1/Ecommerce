from django.contrib import admin

from django.contrib import admin
from .models import Product, CartItem, Cart, Order
from django.db import models

from django.contrib import admin
from .models import Product,Order,CartItem,Cart


class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'image_url')


admin.site.register(Product, ProductAdmin)


class OrdersAdmin(admin.ModelAdmin):

    list_display = ('id', 'cart')


admin.site.register(Order, OrdersAdmin)


class CartItemAdmin(admin.ModelAdmin):

  list_display = ('product', 'cart')


admin.site.register(CartItem, CartItemAdmin)


class CartAdmin(admin.ModelAdmin):

    list_display = ('id',)


admin.site.register(Cart, CartAdmin)





