# object_detection/urls.py

from django.urls import path, include
from .views import item_list, home
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('items/', item_list, name='item_list'),  # URL для отображения списка предметов
    path('', home, name='home'),  # Главная страница
    path('api/', include(router.urls)),  # Убедитесь, что этот путь существует
]
