from flask import Blueprint, request, jsonify
from business.user_business import register_user, check_user_exists, authenticate_user, verify_token

user_api = Blueprint('user_api', __name__)

@user_api.route('/register', methods=['POST'])
def register():
    data = request.json
    if 'username' not in data:
        return jsonify({"error": "Invalid request"}), 400
    token, registered = register_user(data['username'])
    if registered:
        return jsonify({"token": token}), 201
    else:
        return jsonify({"error": "Username already exists"}), 400
    
@user_api.route('/login', methods=['POST'])
def login():
    data = request.json
    if 'username' not in data:
        return jsonify({"error": "Invalid request"}), 400
    
    token, authenticated = authenticate_user(data['username'])
    if authenticated:
        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Invalid username"}), 400

@user_api.route('/user_exists', methods=['GET'])
def user_exists():
    data = request.json
    if 'username' not in data:
        return jsonify({"error": "Invalid request"}), 400
    return jsonify({"exists": check_user_exists(data['username'])}), 200

@user_api.route('/verify', methods=['GET'])
def verify():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Missing token"}), 401

    token = auth_header.split()[1]
    return verify_token(token)