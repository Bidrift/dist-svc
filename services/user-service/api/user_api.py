from flask import Blueprint, request, jsonify
from business.user_business import register_user, check_user_exists

user_api = Blueprint('user_api', __name__)

@user_api.route('/register', methods=['POST'])
def register():
    data = request.json
    if 'username' not in data:
        return jsonify({"error": "Invalid request"}), 400
    if register_user(data['username']):
        return jsonify({"message": "User registered"}), 201
    else:
        return jsonify({"error": "Username already exists"}), 400

@user_api.route('/user_exists', methods=['GET'])
def user_exists():
    data = request.json
    if 'username' not in data:
        return jsonify({"error": "Invalid request"}), 400
    return jsonify({"exists": check_user_exists(data['username'])}), 200