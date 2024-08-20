from django.urls import path
from .views import ProfileAPIView


urlpatterns = [
    path('<int:telegram_id>/', ProfileAPIView.as_view(), name='profile')
]
