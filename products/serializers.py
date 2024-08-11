from rest_framework.serializers import ModelSerializer, ListSerializer
from .models import Product, Category, Order, Basket, ProductImage


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = 'image', 'product'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'name',


class BasketModelSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = 'user', 'product', 'quantity'


class ProductModelSerializer(ModelSerializer):
    image = ListSerializer(child=ProductImageModelSerializer(), source='images')

    class Meta:
        model = Product
        fields = 'id', 'name', 'price', 'description', 'quantity', 'discount', 'category', 'image', 'is_new'


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = 'product', 'user', 'quantity'
