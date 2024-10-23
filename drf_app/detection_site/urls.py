from django.urls import path, include
from rest_framework.routers import DefaultRouter
from object_detection.views import ItemViewSet
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),  # Маршрут для админки
    path('api/', include('object_detection.urls')),  # Подключение маршрутов приложения
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
