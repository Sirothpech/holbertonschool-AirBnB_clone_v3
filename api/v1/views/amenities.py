#!/usr/bin/python3
"""This module contains the amenity class"""


from models.amenity import Amenity
from models import storage
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/amenities/', methods=['GET'], strict_slashes=False)
@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenities(amenity_id=None):
    """Retrieves get method for all amenity"""
    all_amenity = storage.all(Amenity).values()
    if amenity_id is None:
        list_amenity = []
        for amenity in all_amenity:
            list_amenity.append(amenity.to_dict())
        return jsonify(list_amenity)
    else:
        amenity = storage.get(Amenity, amenity_id)
        if amenity is None:
            return jsonify({'error': 'Amenity not found'}), 404
        return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """ Method that deletes a amenity based on its ID. """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return jsonify({'error': 'Amenity not found'}), 404
    amenity.delete()
    storage.save()
    return jsonify({})


@app_views.route('/amenities/', methods=['POST'], strict_slashes=False)
def create_amenity():
    """ Method that creates a new amenity. """
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in request.get_json():
        return jsonify({'error': 'Missing name'}), 400
    new_amenity = Amenity(**request.get_json())
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """ Method that updates a amenity based on its ID. """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return jsonify({'error': 'Amenity not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
