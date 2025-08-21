from django.contrib.auth.models import AbstractBaseUser

from Cart.serializers import AddItemToCartSerializer
from .models import Cart, CartItem
from Products.models import Product


def get_or_create_cart_for_user(user : AbstractBaseUser):
    cart_exists = True if Cart.objects.filter(user = user.pk,
                                            status = "open").exists() else False
    if cart_exists:
        return Cart.objects.get(user = user.pk,
                            status = "open")
    else:
        new_cart = Cart.objects.create(user = user.pk)
        return new_cart

class RemoveItemFromCartService:
    def __init__(self,
                cart : Cart,
                product : Product) -> None:
        self.cart = cart
        self.product = product
    
    def check_if_item_is_in_cart(self):
        for item in self.cart.items:
            if item.product == self.product:
                return True
        return False
    
    def remove_item_from_cart(self):
        for item in self.cart.items:
            if item.product == self.product:
                item.delete()


class UpdateItemFromCartService:
    def __init__(self,
                cart : Cart,
                product : Product,
                new_quantity : int) -> None:
        self.cart = cart
        self.product = product
        self.new_quantity = new_quantity
     
    def check_if_item_is_in_cart(self):
        for item in self.cart.items:
            if item.product == self.product:
                return True
        return False

    def update_item_from_cart(self):
       for item in self.cart.items:
            if item.product == self.product: 
                item.quantity = self.new_quantity
                item.save()

        
class ApplyDiscountThroughCartItemService:
    def __init__(self,
                cart : Cart,
                product : Product,
                code : str) -> None:
        self.cart = cart
        self.product = product
        self.code = code
    
     
    def check_if_item_is_in_cart(self):
        for item in self.cart.items:
            if item.product == self.product:
                return True
        return False

    def apply_discount_through_cart(self):
         for item in self.cart.items:
            if item.product == self.product:
                item.final_price -= self.code.discount_rate * item.final_price
                item.save()


