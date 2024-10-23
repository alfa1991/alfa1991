from flask import Blueprint, request, jsonify
from .models import User, db

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'username': new_user.username, 'age': new_user.age}), 201

@users_blueprint.route('/users/', methods=['GET'])
def read_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'age': user.age} for user in users])

@users_blueprint.route('/users/<int:user_id>/', methods=['GET'])
def read_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'id': user.id, 'username': user.username, 'age': user.age})
