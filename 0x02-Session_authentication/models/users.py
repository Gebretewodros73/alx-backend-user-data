#!/usr/bin/env python3
"""
Module for user-related routes.
"""

from flask import Blueprint, jsonify, request
from models.user import User
users_blueprint = Blueprint('users', __name__, url_prefix='/api/v1/users')


# Create a list to store user data (for demonstration purposes)
users = []


def register_user():
    """
    Register a new user.

    Args:
        None

    Returns:
        Tuple: (response, status code)
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User(email=email, password=password)
    users.append(user)
    return jsonify({'message': 'User registered successfully'}), 201


def get_user(user_id):
    """
    Get user by ID.

    Args:
        user_id (int): User ID.

    Returns:
        Tuple: (response, status code)
    """
    user = next((user for user in users if user.id == user_id), None)
    if user is not None:
        return jsonify({'id': user.id, 'email': user.email}), 200
    else:
        return jsonify({'message': 'User not found'}), 404


def update_user(user_id):
    """
    Update user information.

    Args:
        user_id (int): User ID.

    Returns:
        Tuple: (response, status code)
    """
    user = next((user for user in users if user.id == user_id), None)
    if user is not None:
        data = request.get_json()
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404


def delete_user(user_id):
    """
    Delete user by ID.

    Args:
        user_id (int): User ID.

    Returns:
        Tuple: (response, status code)
    """
    global users
    users = [user for user in users if user.id != user_id]
    return jsonify({'message': 'User deleted successfully'}), 200
