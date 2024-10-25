# object_detection/urls.py

from django.urls import path, include
from .views import item_list_api, home, index
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', index, name='index'),  # Главная страница вашего приложения
    path('home/', home, name='home'),  # Вы можете изменить на другой путь, если хотите
    path('items/api/', item_list_api, name='item_list_api'),  # API для отображения списка предметов
    path('api/', include(router.urls)),  # URL для API
]
