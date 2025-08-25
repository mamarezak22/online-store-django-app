from django.contrib import admin
from .models import Product, Category, ProductImage

class ProductImageInline(admin.TabularInline):
    model = Product.images.through
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title", "category", "price", "discount_rate", "final_price_display",
        "is_available", "view_count", "purchase_count", "created_at"
    )
    list_filter = ("is_available", "category", "created_at")
    search_fields = ("title", "description")
    inlines = [ProductImageInline]
    readonly_fields = ("final_price_display",)

    def final_price_display(self, obj):
        return obj.final_price
    final_price_display.short_description = "Final Price"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    search_fields = ("name",)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("image",)
