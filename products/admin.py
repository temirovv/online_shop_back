from django.contrib.admin import ModelAdmin, register, StackedInline

from .models import Product, ProductImage, Order, Category


class ImageStackedInline(StackedInline):
    model = ProductImage
    fields = 'image', 'product'


@register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = ImageStackedInline,


@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@register(Order)
class OrderModelAdmin(ModelAdmin):
    pass
