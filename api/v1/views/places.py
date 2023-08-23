#!/usr/bin/python3
"""This module contains the Place class"""


from models.user import User
from models.place import Place
from models.city import City
from models import storage
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(city_id):
    """Retrieves get method for all place"""
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify([place.to_dict()for place in city.places])


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_places_id(place_id):
    """Retrieves get method for all places"""
    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """ Method that deletes a place based on its ID. """
    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404
    place.delete()
    storage.save()
    return jsonify({})


@app_views.route('/places/<place_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """ Method that creates a new place. """
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    if 'user_id' not in request.get_json():
        return jsonify({'error': 'Missing user_id'}), 400
    user_id = request.get_json()['user_id']
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'Not found'}), 404
    if 'name' not in request.get_json():
        return jsonify({'error': 'Missing name'}), 400
    new_place = Place(**request.get_json())
    new_place.city_id = city.id
    new_place.user_id = user.id
    new_place.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """ Method that updates a state based on its ID. """
    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({'error': 'Place not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200
