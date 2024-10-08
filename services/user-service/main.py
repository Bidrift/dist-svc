from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    if 'username' not in data or any(u['username'] == data['username'] for u in users):
        return jsonify({"error": "Invalid or duplicate username"}), 400
    users.append({"username": data['username']})
    return jsonify({"message": "User registered"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
