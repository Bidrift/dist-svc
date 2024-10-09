from pymongo import MongoClient, ReturnDocument
from bson.objectid import ObjectId

mongo_username = "root"
mongo_password = "example"
mongo_host = "message-db"
mongo_port = 27017
# Configure your MongoDB connection
mongo_uri = f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/?authSource=admin"

client = MongoClient(mongo_uri)
db = client['like_db'] 
msgdb = client["messagesdb"]
messages_collection = msgdb["messages"]
likes_collection = db['likes'] 

def insert_like(username, message_id, date):
    existing_like = likes_collection.find_one({"username": username, "message_id": message_id})
    if existing_like:
        return False
    
    new_like = {
        "username": username,
        "message_id": message_id,
        "timestamp": date
    }
    likes_collection.insert_one(new_like)
    return True
    
def increment_likes(message_id):
    try:
        result = messages_collection.update_one(
            {'_id': ObjectId(message_id)},
            {'$inc': {'likes': 1}}
        )
        if result.modified_count == 0:
            return {"success": False, "error": "Message not found"}
        return {"success": True, "message": "Message liked"}
    except Exception as e:
        return {"success": False, "error": str(e)}