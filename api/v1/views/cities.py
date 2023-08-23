#!/usr/bin/python3
"""This module contains the State class"""


from models.state import State
from models.city import City
from models import storage
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """Retrieves get method for all state"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify([city.to_dict()for city in state.cities])


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_cities_id(city_id):
    """Retrieves get method for all cities"""
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """ Method that deletes a city based on its ID. """
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    city.delete()
    storage.save()
    return jsonify({})


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """ Method that creates a new city. """
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in request.get_json():
        return jsonify({'error': 'Missing name'}), 400
    new_city = City(**request.get_json())
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """ Method that updates a state based on its ID. """
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict()), 200
