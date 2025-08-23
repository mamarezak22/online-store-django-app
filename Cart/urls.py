from django.urls import path

from Cart.services import RemoveItemFromCartService
from Cart.views import AddItemToCartView, CartDetailView, RemoveItemFromCartView, UpdateItemFromCartView


urlpatterns = [
    path("",CartDetailView.as_view(),name = "cart-detail"),
    path("add-item",AddItemToCartView.as_view(),name="add-item-to-cart"),
    path("remove-item",RemoveItemFromCartView.as_view(),name="remove-item-from-cart"),
    path("update-item",UpdateItemFromCartView.as_view(),name = "update-item-from-cart"),
]