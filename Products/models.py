from django.db import models


class Product(models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField()
    price = models.IntegerField(max_length=16)
    #0 to 1
    discount_rate = models.DecimalField(max_digits=3,decimal_places=2)
    category = models.ForeignKey("Category",on_delete = models.PROTECT,related_name = "products")
    images = models.ManyToManyField("ProductImage")
    is_available = models.BooleanField(default = False)
    view_count = models.IntegerField(default = 0)
    purchase_count = models.IntegerField(default= 0)
    created_at = models.DateTimeField(auto_now_add =  True)
    modified_at = models.DateTimeField(auto_now = True)

    @property
    def final_price(self):
        if self.discount_rate == 0:
            return self.price
        return (1-(self.discount_rate)) * (self.price)
         

class Category(models.Model):
    name = models.CharField(max_length = 128)


class ProductImage(models.Model):
    image = models.FileField(upload_to="product_images/")


class DiscountCode(models.Model):
    code = models.CharField(max_length=100)
    products = models.ManyToManyField(Product) 
    is_active = models.BooleanField(default = True)