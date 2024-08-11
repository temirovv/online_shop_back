from django.urls import path

from .views import ProductListAPIView, ProductDetailAPIView


urlpatterns = [
    path('products', ProductListAPIView.as_view(), name='products'),
    path('product-detail/<int:pk>', ProductDetailAPIView.as_view(), name='product-detail')
]
