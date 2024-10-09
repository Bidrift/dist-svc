from persistence.like_persistence import insert_like, increment_likes, fetch_latest_messages
from datetime import datetime


def like_message(username, message_id):
    date = datetime.now()
    if not insert_like(username, message_id, date):
        return {"success": False, "error": "User has already liked this message."}
    if increment_likes(message_id):
        return {"success": True, "message": "Message liked successfully."}
    return {"success": False, "error": "Failed to update likes count"}

def get_feed_logic():
    return fetch_latest_messages()
    
