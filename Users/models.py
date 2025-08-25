from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,phone_number,username , password = None, **extra_fields):
        user = self.model(phone_number = phone_number,
                          username = username,
                        **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,phone_number,username , password = None,**extra_fields):
        extra_fields.setdefault("is_staff" , True)
        extra_fields.setdefault("is_admin" , True)
        extra_fields.setdefault("is_superuser",True)
        return self.create_user(phone_number,username,password,**extra_fields)

class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=11,unique = True)
    username = models.CharField(max_length=64,null = True)
    is_active  = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)
    is_admin = models.BooleanField(default= False)

    USERNAME_FIELD = 'phone_number' 
    REQUIRED_FIELDS = ("username",)

    objects = UserManager()
