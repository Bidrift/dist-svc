from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

def find_user(username):
    return any(u['username'] == username for u in users)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    if 'username' not in data:
        return jsonify({"error": "Invalid request"}), 400
    if find_user(data['username']):
        return jsonify({"error": "User " + data['username'] + " already exists"}), 400
    users.append({"username": data['username']})
    return jsonify({"message": "User registered"}), 201

@app.route('/user_exists', methods=['GET'])
def user_exists():
    data = request.json
    if 'username' not in data:
        return jsonify({"error": "Invalid request"}), 400
    return jsonify({"exists": find_user(data['username'])}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
