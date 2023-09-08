from flask import request, jsonify
from functools import wraps
import jwt
import json
from datetime import datetime, timedelta

location = 'api/Authentication/key.json'

def write_key():
    """
    writes new key for API
    """
    key = {
        'key': ''
    }
    with open(location, 'w') as json_file:
        json.dump(key, json_file, indent=4)

def read_key():
    """
    returns key for API
    """
    with open(location, 'r') as json_file:
        data = json.load(json_file)
    return data['key']

def token_required(func):
    """
    Decorator for validating user token
    ENSURE INNER FUNCTIONS FIRST PARAMETER IS user_id
    request: HTTP request with token as a header
    """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token_status = validate_token(request)
        try:
            user_id = token_status['user_id']
            request.user_id = user_id
            return func(*args, **kwargs)
        except Exception as e:
            return token_status
        
    return decorated_function  

def validate_token(request):
    """
    Validates token from HTTP request
    request: HTTP request
    returns: int, user_id IF token is valid ELSE JSON response, message
    """
    token = request.headers.get('Authorization', 'NONE')
    
    if not token or not token.startswith('Bearer '):
        return jsonify({'message': 'Token is missing'}), 401
    token = token.replace('Bearer ', '')

    try:
        payload = jwt.decode(token, read_key(), algorithms=['HS256'])
        return {'user_id': payload.get('user_id')}
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.DecodeError:
        return jsonify({'message': 'Invalid token'}), 401
    
def generate_token(user_id) -> str:
    """
    Generates token for client
    user_id: user_id in database
    returns: str, token
    """
    expires = datetime.utcnow() + timedelta(hours=1)
    payload = {
        'user_id': user_id,
        'expires': expires.isoformat()
    }
    token = jwt.encode(payload, read_key(), algorithm='HS256')
    return token

if __name__ == '__main__':
    write_key()