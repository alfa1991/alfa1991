#object_detection/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item  # Импортируйте вашу модель предмета
from .serializers import ItemSerializer  # Импортируйте сериализатор предмета
from django.shortcuts import render
from django.urls import path, include
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter





@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()  # Получаем все предметы
    serializer = ItemSerializer(items, many=True)  # Сериализация предметов
    return Response(serializer.data)  # Возвращаем данные в формате JSON

def home(request):
    return render(request, 'object_detection/home.html')  # Отображение главной страницы

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()  # Запрос всех предметов
    serializer_class = ItemSerializer  # Сериализатор для предметов


router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('items/', item_list, name='item_list'),  # URL для отображения списка предметов
    path('', home, name='home'),  # Главная страница
    path('api/', include(router.urls)),  # Убедитесь, что этот путь существует
]