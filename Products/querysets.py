from .models import Product
from django.db import models

class ProductQuerySet(models.QuerySet):
    def filter_by_category(self, category_id):
        if category_id:
            return self.filter(category__id=category_id)
        return self

    def filter_by_availability(self, is_available):
        if is_available:
            return self.filter(is_available=True)
        return self

    def sort_by_price(self, direction):
        if direction.lower() == 'a':
            return self.order_by('price')
        elif direction.lower() == 'd':
            return self.order_by('-price')
        return self

    def most_viewed(self, active):
        if active:
            return self.order_by('-views')
        return self

    def most_purchased(self, active):
        if active:
            return self.order_by('-purchase_count')
        return self
