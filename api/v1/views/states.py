#!/usr/bin/python3
"""This module contains the State class"""


from models.state import State
from models import storage
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_states(state_id=None):
    """Retrieves get method for all state"""
    all_state = storage.all(State).values()
    if state_id is None:
        list_state = []
        for state in all_state:
            list_state.append(state.to_dict())
        return jsonify(list_state)
    else:
        state = storage.get(State, state_id)
        if state is None:
            return jsonify({'error': 'State not found'}), 404
        return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """ Method that deletes a state based on its ID. """
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({'error': 'State not found'}), 404
    state.delete()
    storage.save()
    return jsonify({})


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create_state():
    """ Method that creates a new state. """
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in request.get_json():
        return jsonify({'error': 'Missing name'}), 400
    new_state = State(**request.get_json())
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ Method that updates a state based on its ID. """
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({'error': 'State not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
