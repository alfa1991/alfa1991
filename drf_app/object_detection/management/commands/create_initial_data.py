# drf_app/object_detection/management/commands/create_initial_data.py

from django.core.management.base import BaseCommand
from object_detection.models import Item

class Command(BaseCommand):
    help = 'Создать начальные данные для приложения object_detection'

    def handle(self, *args, **kwargs):
        if Item.objects.count() == 0:
            Item.objects.create(name='Пример предмета', description='Это пример описания.', price=100.00, category='Продукты')
            self.stdout.write(self.style.SUCCESS('Начальные данные созданы.'))
        else:
            self.stdout.write(self.style.WARNING('Данные уже существуют.'))
