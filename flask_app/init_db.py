# init_db.py

from app import app
from database import init_db
from models import User, db

with app.app_context():
    init_db()  # Инициализация базы данных
    # Добавление пользователей
    user1 = User(username='Alice', age=30)
    user2 = User(username='Bob', age=25)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()  # Сохраняем изменения
