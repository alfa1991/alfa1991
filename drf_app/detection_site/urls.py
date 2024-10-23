from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для административной панели
    path('api/', include('object_detection.urls')),  # Включение URL для приложения object_detection
]
