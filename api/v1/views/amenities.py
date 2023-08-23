#!/usr/bin/python3
"""This module contains the amenity class"""


from models.amenity import Amenity
from models.amenity import amenity
from models.city import City
from models import storage
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/amenities/<amenity_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(amenity_id):
    """Retrieves get method for all amenity"""
    amenity = storage.get(amenity, amenity_id)
    if amenity is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify([city.to_dict()for city in amenity.cities])


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


@app_views.route('/amenities/<amenity_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(amenity_id):
    """ Method that creates a new city. """
    amenity = storage.get(amenity, amenity_id)
    if amenity is None:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in request.get_json():
        return jsonify({'error': 'Missing name'}), 400
    new_city = City(**request.get_json())
    new_city.amenity_id = amenity.id
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """ Method that updates a amenity based on its ID. """
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
