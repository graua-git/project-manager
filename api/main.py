from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Add Access for web app
CORS(app)
CORS(app, resources={r"/*": {'origins': 'http://localhost:3000'}})

@app.route('/')
def default():
    return "Flask API"