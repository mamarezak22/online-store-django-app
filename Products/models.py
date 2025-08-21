from django.db import models

class Product(models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField()
    price = models.CharField(max_length=16)
    category = models.ForeignKey("Category",on_delete = models.PROTECT,related_name = "products")
    images = models.ManyToManyField("ProductImage")
    is_available = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add =  True)
    modified_at = models.DateTimeField(auto_now = True)


class Category(models.Model):
    name = models.CharField(max_length = 128)


class ProductImage(models.Model):
    image = models.FileField(upload_to="product_images/")