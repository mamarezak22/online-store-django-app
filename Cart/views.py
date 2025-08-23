from rest_framework.response import Response
from rest_framework.views import APIView

from Cart.serializers import CartSerializer, CartItemSerializer, RemoveItemFromCartSerializer

from .models import CartItem
from .services import RemoveItemFromCartService, UpdateItemFromCartService, get_or_create_cart_for_user  

#cart/
class CartDetailView(APIView):
    def get(self,request):
        cart = get_or_create_cart_for_user(request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data,
                       status = 200)

#cart/add-item
class AddItemToCartView(APIView):
    def post(self,request):
        cart = get_or_create_cart_for_user(request.user)
        serializer = CartItemSerializer(data = request.data) 
        serializer.is_valid(raise_exception=True)
        #we give the data that serializer has to function to get that and do the computation (data -> product & quantity)
        CartItem.objects.create(cart = cart,
                                product = serializer.validated_data["product"],
                                quantity = serializer.validated_data["quantity"]) 
        return Response({"detail" : "item added to cart"},
                        status = 200)

#cart/remove-item
class RemoveItemFromCartView(APIView):
    def post(self,request):
        cart = get_or_create_cart_for_user(request.user)
        serializer = RemoveItemFromCartSerializer(data = request.data) 
        serializer.is_valid(raise_exception=True)
        service = RemoveItemFromCartService(cart,serializer.validated_data["product"])
        if not service.check_if_item_is_in_cart():
            return Response({"detail" : "item is not in cart to be removed"},
                            status = 400)
        service.remove_item_from_cart()
        return Response({"detail" : "item deleted sucsessfully"},
                        status = 200)

#cart/update-item
class UpdateItemFromCartView(APIView):
    def patch(self,request):
        cart = get_or_create_cart_for_user(request.user)
        serializer = CartItemSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        service = UpdateItemFromCartService(cart,
                                            serializer.validated_data["product"],
                                            serializer.validated_data["quantity"])
        if not service.check_if_item_is_in_cart():
            return Response({"detail" : "item is not in cart to be updated"},
                            status = 400)
        service.update_item_from_cart()
        return Response({"detail" : "item updated sucsessfully"},
                        status = 200)

        
      

    