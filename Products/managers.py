from django.db import models
from .querysets import ProductQuerySet

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    # Optional: expose your custom methods directly on the manager
    def search(self, text):
        return self.get_queryset().search(text)

    def filter_by_category(self, category_id):
        return self.get_queryset().filter_by_category(category_id)

    def filter_by_availability(self, is_available):
        return self.get_queryset().filter_by_availability(is_available)

    def sort_by_value(self, value):
        return self.get_queryset().sort_by_value(value)