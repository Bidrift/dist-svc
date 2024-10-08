from persistence.message_persistence import insert_message, fetch_latest_messages

def post_message_logic(username, message):
    if not message:
        return {"error": "Message content is missing"}
    
    if len(message) > 400:
        return {"error": "Message is too long"}

    return insert_message(username, message)

def get_feed_logic():
    return fetch_latest_messages()