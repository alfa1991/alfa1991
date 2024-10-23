# database.py

from flask import Flask
from models import db

def init_db(app: Flask):
    with app.app_context():
        db.init_app(app)
        db.create_all()  # Создаем все таблицы из моделей
