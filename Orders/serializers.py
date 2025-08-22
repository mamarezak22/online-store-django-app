from rest_framework import serializers
from Cart.models import Cart
from Products.models import DiscountCode
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class ApplyDiscountToOrderSerializer(serializers.Serializer):
    discount_code = serializers.PrimaryKeyRelatedField(queryset = DiscountCode.objects.all()) 
