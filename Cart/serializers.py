from rest_framework import serializers

from Products.models import Product
from Cart.models import Cart , CartItem

class CartItemSerializer(serializers.Serializer):
    #Accept a product ID in the request
    #Validate that it exists in the Product table through queryset
    #and the intersting part is that product now is not the id but the actual instance from queryset takes place.
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(default = 1)

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cartitem_set', many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']
