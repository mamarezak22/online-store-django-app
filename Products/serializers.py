from rest_framework import serializers

from Products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title","description","category","price","discount_rate","final_price","images","is_available","view_count","purchase_count","star"] 