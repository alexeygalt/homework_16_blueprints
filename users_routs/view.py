from flask import Blueprint, jsonify, request
from db.models import db, User

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users/', methods=['GET', 'POST'])
def get_all_users():
    if request.method == 'GET':
        users = User.query.all()
        result = []
        for user in users:
            result.append(user.users_to_dict())
        return jsonify(result)

    if request.method == 'POST':
        upload_user = request.get_json()
        new_user = User(
            first_name=upload_user.get('first_name'),
            last_name=upload_user.get('last_name'),
            age=upload_user.get('age'),
            email=upload_user.get('email'),
            role=upload_user.get('role'),
            phone=upload_user.get('phone')
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.users_to_dict())


@users_blueprint.route('/users/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def get_one_user(pk):
    user = User.query.get(pk)
    if not User.query.get(pk):
        return jsonify({'ValueError': 'user not found'})
    if request.method == 'GET':
        return jsonify(user.users_to_dict())
    if request.method == 'PUT':
        upload_user = request.get_json()
        user.first_name = upload_user.get('first_name')
        user.last_name = upload_user.get('last_name')
        user.age = upload_user.get('age')
        user.email = upload_user.get('email')
        user.role = upload_user.get('role')
        user.phone = upload_user.get('phone')
        db.session.add(user)
        db.session.commit()
        return jsonify(user.users_to_dict())
    if request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify({f'User {pk}': 'deleted'})
