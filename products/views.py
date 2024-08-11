from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Category, Product, Order, Basket
from .serializers import ProductModelSerializer, OrderModelSerializer, BasketModelSerializer
from .filters import ProductModelFilterSet



class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filterset_class = ProductModelFilterSet


class ProductDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductModelSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderAPIView(APIView):
    permission_classes = IsAuthenticated,

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderModelSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
