#!/usr/bin/env python3
"""
Route module for the API.
"""
import os
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)

from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth

class User:
    """User class for authentication."""
    def __init__(self):
        self.id = None

    def current_user(self, request):
        """Return the current user based on request."""
        return self.id

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = getenv('AUTH_TYPE', 'auth')
if auth_type == 'auth':
    auth = Auth()
if auth_type == 'basic_auth':
    auth = BasicAuth()


class User:
    """User class for authentication."""
    def __init__(self):
        self.id = None

    def current_user(self, request):
        """Return the current user based on request."""
        return self.id

    def is_valid(self, user_id):
        """Check if a user ID is valid."""
        # Add your logic to validate the user ID here
        return True  # Return True if the user ID is valid, otherwise return False

    def is_admin(self, user_id):
        """Check if a user is an admin."""
        # Add your logic to check if the user is an admin here
        return False  # Return True if the user is an admin, otherwise return False


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler.
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized handler.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden handler.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def authenticate_user():
    """Authenticates a user before processing a request.
    """
    user = User()
    if auth:
        excluded_paths = [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/',
        ]
        if auth.require_auth(request.path, excluded_paths):
            auth_header = auth.authorization_header(request)
            user.id = auth.current_user(request)
            if auth_header is None:
                abort(401)
            if user.id is None:
                abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
