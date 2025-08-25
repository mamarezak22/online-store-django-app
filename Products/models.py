from django.db import models

from datetime import timedelta

from Products.managers import ProductManager


class Product(models.Model):
    title = models.CharField(max_length = 128,db_index= True)
    description = models.TextField()
    price = models.IntegerField()
    final_price = models.IntegerField(null = True,blank= True)
    #0 to 1
    discount_rate = models.DecimalField(max_digits=3,decimal_places=2,default = 0)
    category = models.ForeignKey("Category",on_delete = models.PROTECT,related_name = "products")
    images = models.ManyToManyField("ProductImage",null = True,blank = True)
    is_available = models.BooleanField(default = True)
    view_count = models.IntegerField(default = 0)
    purchase_count = models.IntegerField(default= 0)
    star = models.DecimalField(max_digits=3,decimal_places=2,default = 0)
    created_at = models.DateTimeField(auto_now_add =  True)
    modified_at = models.DateTimeField(auto_now = True)
    
    objects = ProductManager()

    def save(self,*args,**kwargs):
        self.final_price = (1 - self.discount_rate)    * (self.price)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title
         

class Category(models.Model):
    name = models.CharField(max_length = 128)
    #if parent == null it means it is a main category and not a sub category.
    parent = models.ForeignKey("Category",on_delete= models.CASCADE , null = True,blank = True)
    
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.FileField(upload_to="product_images/")


class DiscountCode(models.Model):
    code = models.CharField(max_length=100,primary_key=True)
    # 0 to 1
    discount_rate = models.DecimalField(max_digits=3,decimal_places=2)
      #some discount codes have price limits.
    is_limited_to_price = models.BooleanField(default= False)
    minimum_price_to_cover = models.IntegerField(null = True)
    maximum_price_to_cover = models.IntegerField(null = True) 
    created_at = models.DateTimeField(auto_now_add = True)
    expire_time = models.PositiveIntegerField(null = True,help_text = "in hours",default = 24)

    @property
    def is_active(self):
        if self.expire_time:
            return self.created_at + timedelta(hours = self.expire_time) 
        return True 
