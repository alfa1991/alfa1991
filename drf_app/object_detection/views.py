from django.shortcuts import render
from .models import Item  # Импортируем модель Item

def item_list(request):
    items = Item.objects.all()  # Получаем все предметы из базы данных
    return render(request, 'item_list.html', {'items': items})  # Отправляем предметы в шаблон
