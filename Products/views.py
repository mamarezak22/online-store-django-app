from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny
from Products.models import Product
from Products.paginators import CustomPageNumberPagination
from .services import get_products_based_on_query_params 
from .serializers import ProductSerializer


#products?category={category_id}&sort_by_price={d or a}  <optional ones> &is_available&most_view&most_purchase
class ProductListView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        products = get_products_based_on_query_params(request.query_params)
        paginator = CustomPageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(products, request, view=self)
        
        # Serialize paginated data
        serializer = ProductSerializer(paginated_queryset, many=True)
        
        # Return paginated response
        return paginator.get_paginated_response(serializer.data)
         
class ProductDetailView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request,product_id):
        product = get_object_or_404(Product,pk = product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data,
                        status = 200) 

