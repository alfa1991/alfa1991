from flask import Blueprint, jsonify, request
from models import db, User

users_blueprint = Blueprint('users', __name__)

# Получение списка пользователей
@users_blueprint.route('/users/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'age': user.age} for user in users]), 200

# Получение конкретного пользователя
@users_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"detail": "User not found"}), 404
    return jsonify({'id': user.id, 'username': user.username, 'age': user.age}), 200

# Создание нового пользователя
@users_blueprint.route('/users/', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'username': new_user.username, 'age': new_user.age}), 201

# Обновление пользователя
@users_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"detail": "User not found"}), 404
    data = request.json
    user.username = data.get('username', user.username)
    user.age = data.get('age', user.age)
    db.session.commit()
    return jsonify({'id': user.id, 'username': user.username, 'age': user.age}), 200

# Удаление пользователя
@users_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"detail": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"detail": "User deleted"}), 204
