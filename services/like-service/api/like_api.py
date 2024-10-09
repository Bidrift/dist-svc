from flask import Blueprint, request, jsonify
from business.like_business import like_message, get_feed_logic
import requests

like_api = Blueprint('like_api', __name__)

USER_SERVICE_URL = 'http://user-service:5000'

def verify_user(token):
    headers = {'Authorization': f'Bearer {token}'}
    print(USER_SERVICE_URL)
    response = requests.get(f'{USER_SERVICE_URL}/verify', headers=headers)
    if response.status_code == 200:
        return response.json().get('username')
    return None

@like_api.route('/like', methods=['POST'])
def like():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Authorization header missing"}), 401

    username = verify_user(auth_header.split()[1])
    if not username:
        return jsonify({"error": "Unauthorized"}), 403
    data = request.json
    message_id = data.get('message_id')
    if not message_id:
        return jsonify({"error": "Message ID is required."}), 400

    response = like_message(username, message_id)

    if response['success']:
        return jsonify(response), 200
    else:
        return jsonify(response), 400
    
@like_api.route('/feed', methods=['GET'])
def get_feed():
    result = get_feed_logic()
    return jsonify(result), 200
