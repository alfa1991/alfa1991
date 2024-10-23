from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import users_blueprint  # Импорт маршрутов из views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # Настройка базы данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Подключение маршрутов
app.register_blueprint(users_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
