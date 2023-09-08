from flask import Blueprint, request, jsonify

from Authentication.authentication import token_required
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
    return read("SELECT * FROM Projects")

@projects_bp.route('/read-one', methods=['GET'])
def read_one_project():
    """
    Returns the following table
    project_id | email | first_name | last_name
    """
    return read(f"SELECT * FROM Projects WHERE project_id = {id}", "one")

@projects_bp.route('/myprojects', methods=['GET'])
@token_required
def read_myprojects():
    """
    Returns the projects belonging to a specific user
    project | creator
    """
    user_id = request.user_id

    sql = f"SELECT project_id, name, owner \
            FROM Projects \
            JOIN Memberships ON Memberships.project = Projects.project_id \
            JOIN Users ON Users.user_id = Memberships.user \
            JOIN (SELECT project, creator, CONCAT(Users.first_name, ' ', Users.last_name) as owner \
            FROM Memberships \
            JOIN Users ON Users.user_id = Memberships.user \
            WHERE creator = 1) as Creators ON Projects.project_id = Creators.project \
            WHERE Users.user_id = {user_id};"
    return read(sql)
