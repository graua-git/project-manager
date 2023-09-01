from flask import Flask
from flask_cors import CORS

from Blueprints.users import users_bp
from Blueprints.projects import projects_bp

app = Flask(__name__)

# Add Access for web app
CORS(app)
CORS(app, resources={r"/*": {'origins': 'http://localhost:3000'}})

# Register Blueprints
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(projects_bp, url_prefix='/projects')

if __name__ == '__main__':
    app.run(debug=True)