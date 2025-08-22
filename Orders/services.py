from django.contrib.auth.models import AbstractBaseUser
from Cart.models import Cart, User
from Products.models import DiscountCode
from orders.models import Order, OrderItem

def create_order_from_cart(cart : Cart):
    new_order = Order(user = cart.user,
                        final_price = cart.total_price)
    for item in cart.items:
        OrderItem.objects.create(order = new_order,
                                product = item.product,
                                quantity= item.quantity)
    return new_order

def get_last_not_paid_order_of_user(user : AbstractBaseUser):
    if len(user.orders) == 0:
        return None
    order =  user.orders.order_by("-created_at")[0]
    if order.status == "created":
        return order
    return None

class ApplyDiscountToOrderService:
    def __init__(self,
                order : Order,
                discount_code : DiscountCode) -> None:
        self.order = order
        self.discount_code = discount_code
    
    def can_discount_cover_order_price(self):
        #beautifully spekaing if code is limited to price and order price is more than maximum or less than minimum.
        if self.discount_code.is_limited_to_price and self.discount_code.minimum_price_to_cover > self.order.final_price or self.discount_code.maximum_price_to_cover < self.order.final_price:
            return False
        return True

    def apply_discount_code_and_get_detail_resp(self):
        if self.discount_code.is_limited_to_price:
            if self.discount_code.minimum_price_to_cover > self.order.final_price :
                detail_resp , status = f"minimum price for code to cover is {self.discount_code.minimum_price_to_cover}" , 400
            else:
                detail_resp ,status = f"maximum price for code to cover is {self.discount_code.maximum_price_to_cover}" , 400
        else:
            self.order.price -= (self.discount_code.discount_rate) * (self.order.final_price)
            self.order.save()
            detail_resp , status = "code applied sucsessfully" , 200
        return detail_resp  , status