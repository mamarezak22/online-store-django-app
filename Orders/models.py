from Products.models import Product
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
STATUS_CHOICES = [
        ('created', 'Created'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
]    

class OrderItem(models.Model):
    order = models.ForeignKey("Order",on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name="orders")
    final_price = models.IntegerField()
    status = models.CharField(choices = STATUS_CHOICES,
                                default = "created")
    created_at = models.DateTimeField(auto_now_add=True)
