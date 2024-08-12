from django.contrib.auth import get_user_model, login
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

from .models import Category, Product, Order, Basket
from .serializers import ProductModelSerializer, OrderModelSerializer, BasketModelSerializer
from .filters import ProductModelFilterSet


User = get_user_model()


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filterset_class = ProductModelFilterSet

    def get(self, request, *args, **kwargs):
        telegram_id = request.GET.get('telegram_user_id')

        if not telegram_id:
            return HttpResponseForbidden('Forbidden: Telegram user ID is missing')

        try:
            user = User.objects.get(telegram_id=telegram_id)
            login(request, user)
            return self.list(request, *args, **kwargs)

        except User.DoesNotExist:
            return HttpResponseForbidden('Forbidden: User fount')


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


class BasketAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(request.user)
        return Response('just response')
