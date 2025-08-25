from django.db import models
from django.shortcuts import get_object_or_404

class ProductQuerySet(models.QuerySet):
    def search(self, text):
        if text:
            return self.filter(title__icontains = text)
        return self

    def filter_by_category(self, category):
        #cicular problems make that import happen here . dont suprise pls
        from Products.models import Category
        if category:
            category_obj = get_object_or_404(Category,name = category)
            return self.filter(category__id=category_obj.id)
        return self

    def filter_by_availability(self, is_available):
        if is_available:
            return self.filter(is_available=True)
        return self

    def sort_by_value(self, value):
        if value == "price_desc":
            return self.order_by("-final_price")
        elif value == "price_asc":
            return self.order_by("final_price")
        elif value == "view":
            return self.order_by("-view_count")
        elif value == "purchase":
            return self.order_by("-purchase_count")
        elif value == "star":
            return self.order_by("-star")
        else:
            return self