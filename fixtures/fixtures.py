import pytest
from Products.models import Category,Product
from django.contrib.auth import get_user_model


User = get_user_model()

@pytest.fixture
def product():
    category =  Category.objects.create(name = "heidar baba")
    return Product.objects.create(
                    title = "jfkjfsk",
                    description = "fjkesjfk",
                    price = 600000,
                   category = category)

@pytest.fixture
def user():
    return User.objects.create_user(username = "mamad",
                phone_number = "09162939040",
                password = "12345678")