from django_filters import FilterSet

from .models import Product, Category


class ProductModelFilterSet(FilterSet):
    class Meta:
        model = Product
        fields = 'name', 'price', 'category'
