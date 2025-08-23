from rest_framework.views import APIView, Response

from Cart.services import get_or_create_cart_for_user
from Orders.serializers import ApplyDiscountToOrderSerializer, OrderSerializer
from Orders.services import ApplyDiscountToOrderService, create_order_from_cart, get_last_not_paid_order_of_user

#based on last cart that user creates and have now it create a order from it.

#orders/get-order
class OrderDetailView(APIView):
    def get(self,request):
        last_order = get_last_not_paid_order_of_user(request.user)
        if not last_order:
            return Response({"detail" : "there is no order"},
                            status = 400)
        serializer = OrderSerializer(last_order) 
        return Response(serializer.data,
                        status = 200)
        

class OrderCreateView(APIView):
    def post(self,request):
        cart = get_or_create_cart_for_user(request.user) 
        if cart.isempty():
            return Response({"detail" : "cart is empty"},
                            status = 400)

        last_order = get_last_not_paid_order_of_user(request.user)
        if last_order:
            if last_order.status == "created":
                return Response({"detail" : "last order not paid"},
                            status = 400)

        create_order_from_cart(cart)
        return Response({"detail":"order created sucsessfully"},
                    status = 200)

class ApplyDiscountToOrderView(APIView):
    def post(self,request):
        order = get_last_order_of_user(request.user)
        if not order:
            return Response({"detail" : "there is no order to code be applied"},
                            status = 400)

        serializer = ApplyDiscountToOrderSerializer(data = request.data) 
        code = serializer.validated_data["discount_code"]
        if not code.is_active:
            return Response({"detail" : "code expired"},
                            status = 400)
        service = ApplyDiscountToOrderService(order,code) 
        detail_resp , status = service.apply_discount_code_and_get_detail_resp()
        return Response({"detail" : detail_resp},
                        status = status)

        
        
