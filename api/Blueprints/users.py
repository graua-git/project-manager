from flask import Blueprint, request, jsonify
from pprint import pprint

from Database.crud import read

users_bp = Blueprint('users', __name__)

@users_bp.route('/create-account', methods=['POST'])
def create_user():
    """
    """
    raise NotImplemented

@users_bp.route('/read-all', methods=['GET'])
def read_users():
    """
    Returns the following table
    user_id | email | first_name | last_name
    """
    return read("Read Users")
