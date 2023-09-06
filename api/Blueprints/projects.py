from flask import Blueprint, request, jsonify

from Authentication.authentication import generate_token, validate_token
from Database.crud import create, read, update, delete

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/create', methods=['POST'])
def create_project():
    """
    Creates project, requires info from json
    """
    return create(request.get_json(), "Projects")

@projects_bp.route('/read-all', methods=['GET'])
def read_all_projects():
    """
    Returns the following table
    project_id | email | first_name | last_name
    """
    return read("Read Projects")

@projects_bp.route('/read-one', methods=['GET'])
def read_one_project():
    """
    Returns the following table
    project_id | email | first_name | last_name
    """
    return read("Read Projects", "one")
