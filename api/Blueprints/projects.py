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

@projects_bp.route('/myprojects', methods=['GET'])
def read_myprojects():
    """
    Returns the projects belonging to a specific user
    project | creator
    """
    token_status = validate_token(request)
    try:
        user_id = token_status['user_id']
    except KeyError:
        return validate_token(request)
    
    sql = f"SELECT name, owner \
            FROM Projects \
            JOIN Memberships ON Memberships.project = Projects.project_id \
            JOIN Users ON Users.user_id = Memberships.user \
            JOIN (SELECT project, creator, CONCAT(Users.first_name, ' ', Users.last_name) as owner \
            FROM Memberships \
            JOIN Users ON Users.user_id = Memberships.user \
            WHERE creator = 1) as Creators ON Projects.project_id = Creators.project \
            WHERE Users.user_id = {user_id};"
    return read(sql)
