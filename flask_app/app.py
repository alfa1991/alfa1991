# app.py

from flask import Flask, render_template
from config import Config
from models import db, User
from database import init_db

app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных
init_db(app)

@app.route('/')
def index():
    return "Welcome to the Flask app!"

@app.route('/users/')
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/add_user/<username>/<int:age>/')
def add_user(username, age):
    new_user = User(username=username, age=age)
    db.session.add(new_user)
    db.session.commit()
    return f'Added user {username}!'


if __name__ == '__main__':
    app.run(debug=True)
