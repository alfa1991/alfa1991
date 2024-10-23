from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.views.generic import ListView

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemListView(ListView):
    model = Item
    template_name = 'object_detection/item_list.html' # Шаблон для отображения списка