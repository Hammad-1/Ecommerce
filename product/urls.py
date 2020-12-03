from django.urls import path
from . import views

urlpatterns = [
    path('', views.product),
    path('show_cart/', views.show_cart),
]
