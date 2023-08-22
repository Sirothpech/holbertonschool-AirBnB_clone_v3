#!/usr/bin/python3
""" Module for the app view """
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """HBNB status"""
    return jsonify({'status': 'OK'})
