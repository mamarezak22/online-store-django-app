from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

STATUS_CHOICES = (
    ('open', 'Open'),
    ('close', 'Close'),
)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name="carts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices= STATUS_CHOICES, default="open",help_text="open, close")

    @property
    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart , on_delete= models.CASCADE , related_name="items")
    product = models.ForeignKey("Products.Product",on_delete=models.CASCADE ,null=True)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

