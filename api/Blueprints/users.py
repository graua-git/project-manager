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
def read_all_users():
    """
    Returns the following table
    user_id | email | first_name | last_name
    """
    sql = "SELECT user_id, email, first_name, last_name FROM Users"
    return read(sql)

@users_bp.route('/read-one', methods=['GET'])
def read_one_user():
    """
    Returns the following table
    user_id | email | first_name | last_name
    """
    token_status = validate_token(request)
    try:
        user_id = token_status['user_id']
    except KeyError:
        return validate_token(request)

    sql = f"SELECT user_id, email, first_name, last_name FROM Users WHERE user_id = {user_id}"
    return read(sql, 'one')

@users_bp.route('/login', methods=['POST'])
def login():
    """
    Validates user credentials and generates a token
    """
    # Validate User
    user = request.get_json()
    sql = f"SELECT user_id FROM Users WHERE email = '{user['email']}' AND password = '{user['password']}'"
    try:
        user_id = read(sql, 'one')['user_id']
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    # Generate Token
    token = generate_token(user_id)
    return jsonify({'token': token})

@users_bp.route('/update', methods=['PUT'])
def update_user():
    """
    Updates user with id from token given data from json
    """
    # Validate token
    token_status = validate_token(request)
    try:
        user_id = token_status['user_id']
    except KeyError:
        return validate_token(request)

    # Query database
    return update(request.get_json(), "Users", user_id)

@users_bp.route('/delete', methods=['DELETE'])
def delete_user():
    """
    Deletes user with id from token
    """
    # Validate token
    token_status = validate_token(request)
    try:
        user_id = token_status['user_id']
    except KeyError:
        return validate_token(request)

    # Query database
    return delete(request.get_json(), "Users", user_id)
