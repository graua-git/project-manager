from flask import Blueprint, request, jsonify

from Authentication.authentication import token_required
from Database.crud import create, read, update, delete

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/read/by-project/<int:project_id>', methods=['GET'])
@token_required
def read_by_project(project_id):
    """
    Returns the following table
    TODO: write columns for table
    """
    user_id = request.user_id
    return read(f"SELECT * FROM Tasks WHERE project = {project_id} AND EXISTS \
                (SELECT * FROM Memberships WHERE project = {project_id} AND user = {user_id}) \
                ORDER BY date_created DESC, time_created")
