from flask import Blueprint, request, jsonify

from Authentication.authentication import generate_token, validate_token
from Database.crud import create, read, update, delete

users_bp = Blueprint('users', __name__)

@users_bp.route('/create-account', methods=['POST'])
def create_user():
    """
    Creates user, requires info from json
    """
    return create(request.get_json(), "Users")

@users_bp.route('/read-all', methods=['GET'])
def read_users():
    """
    Returns the following table
    user_id | email | first_name | last_name
    """
    return read("Read Users")

@users_bp.route('/login', methods=['POST'])
def login():
    """
    Validates user credentials and generates a token
    """
    # Validate User
    user = request.get_json()
    sql = f"SELECT user_id FROM Users WHERE email = '{user['email']}' AND password = '{user['password']}'"
    headers = ['user_id']
    try:
        user_id = read(sql, headers, 'one')['user_id']
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Generate Token
    token = generate_token(user_id)
    return jsonify({'token': token})

@users_bp.route('/update', methods=['POST'])
def update_user():
    # Validate token
    token_status = validate_token(request)
    try:
        user_id = token_status['user_id']
    except KeyError:
        return validate_token(request)

    # Query database
    return update(request.get_json(), "Users", user_id)

@users_bp.route('/delete', methods=['DELETE'])
def delete_user(user_id):
    # Validate token
    token_status = validate_token(request)
    try:
        user_id = token_status['user_id']
    except KeyError:
        return validate_token(request)

    # Query database
    return delete(request.get_json(), "Users", user_id)
