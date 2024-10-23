#asgi.py

import os
from django.core.asgi import get_asgi_application

# Установка переменной окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'detection_site.settings')

# Получение ASGI-приложения
application = get_asgi_application()
