users = []

def add_user(username):
    users.append({"username": username})

def find_user(username):
    for user in users:
        if user['username'] == username:
            return user
    return None
