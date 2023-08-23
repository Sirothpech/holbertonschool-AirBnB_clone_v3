#!/usr/bin/python3
"""This module contains the users class"""


from models.user import User
from models import storage
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/users/', methods=['GET'], strict_slashes=False)
@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_users(user_id=None):
    """Retrieves get method for all users"""
    all_users = storage.all(User).values()
    if user_id is None:
        list_user = []
        for user in all_users:
            list_user.append(user.to_dict())
        return jsonify(list_user)
    else:
        user = storage.get(User, user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """ Method that deletes a user based on its ID. """
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    user.delete()
    storage.save()
    return jsonify({})


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
def create_user():
    """ Method that creates a new user. """
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    if 'email' not in request.get_json():
        return jsonify({'error': 'Missing email'}), 400
    if 'password' not in request.get_json():
        return jsonify({'error': 'Missing password'}), 400
    new_user = User(**request.get_json())
    new_user.save()
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def update_user(user_id):
    """ Method that updates a user based on its ID. """
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200
