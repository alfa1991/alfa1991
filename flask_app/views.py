# views.py

from flask import Flask, request, jsonify
from models import db, User
from app import app
from flask import render_template, Flask

app = Flask(__name__)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.json.get('username')
    email = request.json.get('email')

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User added"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users]), 200

@app.route('/')
def home():
    return render_template('index.html')  # Страница по умолчанию

@app.route('/users/')
def users():
    users = User.query.all()  # Получаем всех пользователей из базы данных
    return render_template('users.html', users=users)  # Передаем пользователей в шаблон