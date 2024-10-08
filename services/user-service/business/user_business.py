from persistence.user_persistence import add_user, find_user

def register_user(username):
    if find_user(username):
        return False
    add_user(username)
    return True

def check_user_exists(username):
    return find_user(username) is not None