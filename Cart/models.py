from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.PROTECT)
    items = models.ManyToManyField("Products.Product")


class CartItem(models.Model):
    product = models.ForeignKey("Products.Product",on_delete=models.SET_NULL) 
    quantity = models.PositiveIntegerField()
