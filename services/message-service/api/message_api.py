from flask import Blueprint, request, jsonify
from business.message_business import post_message_logic, get_feed_logic
import requests

message_api = Blueprint('message_api', __name__)

USER_SERVICE_URL = 'http://user-service:5000'

def verify_user(token):
    headers = {'Authorization': f'Bearer {token}'}
    print(USER_SERVICE_URL)
    response = requests.get(f'{USER_SERVICE_URL}/verify', headers=headers)
    if response.status_code == 200:
        return response.json().get('username')
    return None

@message_api.route('/send', methods=['POST'])
def post_message():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Authorization header missing"}), 401

    username = verify_user(auth_header.split()[1])
    if not username:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.json
    result = post_message_logic(username, data.get('message'))
    return jsonify(result), 201 if 'message' in result else 400


@message_api.route('/feed', methods=['GET'])
def get_feed():
    result = get_feed_logic()
    return jsonify(result), 200