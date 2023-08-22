#!/usr/bin/python3
""" Module for the app view """
from flask import Response
from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models
import json


@app_views.route('/status', strict_slashes=False)
def return_status():
    response_data = {"status": "OK"}
    response = Response(json.dumps(response_data),
                        content_type='application/json')
    return response


@app_views.route('/stats', strict_slashes=False)
def stats():
    """HBNB stats"""
    hbnb_class = {
        'amenities': models.storage.count(Amenity),
        'cities': models.storage.count(City),
        'places': models.storage.count(Place),
        'reviews': models.storage.count(Review),
        'states': models.storage.count(State),
        'users': models.storage.count(User)
    }
    return hbnb_class
