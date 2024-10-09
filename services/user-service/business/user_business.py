import jwt
import datetime
import os
from flask import jsonify
from persistence.user_persistence import add_user, find_user

SECRET_KEY = os.getenv('JWT_SECRET', 'default_secret')

def register_user(username):
    if find_user(username):
        return None, False
    add_user(username)
    return generate_token(username), True

def authenticate_user(username):
    user = find_user(username)
    if user:
        return generate_token(username), True
    return None, False

def generate_token(username):
    expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    token = jwt.encode(
        {"username": username, "exp": expiration_time},
        SECRET_KEY,
        algorithm="HS256"
    )
    return token

def verify_token(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"username": decoded_token["username"]}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Expired token"}), 403
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 403

def check_user_exists(username):
    return find_user(username) is not None