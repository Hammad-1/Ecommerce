from django.db import models

from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=128)
    price = models.IntegerField()
    image_url = models.URLField()


class Cart(models.Model):
    pass


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)


