# config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Используйте SQLite для простоты
    SQLALCHEMY_TRACK_MODIFICATIONS = False
