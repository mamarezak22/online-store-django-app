from django.urls import path

from Orders.services import ApplyDiscountToOrderService
from Orders.views import ApplyDiscountToOrderView, OrderCreateView, OrderDetailView


urlpatterns  = [
    path("get-order",OrderDetailView.as_view(),name = "order-detail"),
    path("create-order",OrderCreateView.as_view(),name = "order-create"),
    path("apply-discount",ApplyDiscountToOrderView.as_view(),name = "apply-discount-to-order"),
]