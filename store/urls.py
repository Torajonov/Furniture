from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),


    path('store', views.store, name="store"),
    path('checkout', views.checkout, name="checkout"),
    path('cart', views.cart, name="cart"),

    path('update_item/', views.updateItem, name="updateItem"),
    path('process_order/', views.processOrder, name="processOrder"),
]
