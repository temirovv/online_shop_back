from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
