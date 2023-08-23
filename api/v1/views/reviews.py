#!/usr/bin/python3
"""This module contains the Review class"""


from models.user import User
from models.place import Place
from models.review import Review
from models import storage
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """Retrieves get method for all reviews"""
    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify([review.to_dict()for review in place.reviews])


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_reviews_id(review_id):
    """Retrieves get method for all reviews"""
    review = storage.get(Review, review_id)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """ Method that deletes a review based on its ID. """
    review = storage.get(Review, review_id)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    review.delete()
    storage.save()
    return jsonify({})


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """ Method that creates a new review. """
    place = storage.get(Place, place_id)
    if place is None:
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
    new_review = Review(**request.get_json())
    new_review.place_id = place.id
    new_review.user_id = user.id
    new_review.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """ Method that updates a state based on its ID. """
    review = storage.get(Review, review_id)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
