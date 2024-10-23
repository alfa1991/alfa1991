import os
from django.core.wsgi import get_wsgi_application

# Установка переменной окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'detection_site.settings')

# Получение WSGI-приложения
application = get_wsgi_application()
