from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from .models import User
from .serializers import UserModelSerializer


class ProfileAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'telegram_id'
