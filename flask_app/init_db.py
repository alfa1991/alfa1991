# init_db.py

from app import app  # Импортируем ваше приложение Flask
from database import init_db  # Импортируем функцию инициализации базы данных

with app.app_context():  # Создаем контекст приложения
    init_db()  # Вызываем функцию инициализации базы данных
