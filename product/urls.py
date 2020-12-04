from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('show_cart/', views.show_cart, name='showcart'),
    path('checkout/', views.checkout, name='checkout')
]
