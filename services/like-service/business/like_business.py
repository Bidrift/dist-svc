from persistence.like_persistence import insert_like, increment_likes
from datetime import datetime


def like_message(username, message_id):
    date = datetime.now()
    if not insert_like(username, message_id, date):
        return {"success": False, "error": "User has already liked this message."}
    return increment_likes(message_id)
    
