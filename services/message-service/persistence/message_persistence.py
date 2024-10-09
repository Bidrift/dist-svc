from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_username = "root"
mongo_password = "example"
mongo_host = "message-db"
mongo_port = 27017

mongo_uri = f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/?authSource=admin"

# Initialize MongoDB client and collection
client = MongoClient(mongo_uri)
db = client["messagesdb"]
messages_collection = db["messages"]

def insert_message(username, message):
    new_message = {
        "username": username,
        "message": message,
        "likes": 0
    }
    result = messages_collection.insert_one(new_message)
    return {"message": "Message posted", "id": str(result.inserted_id)}

def fetch_latest_messages():
    messages = list(messages_collection.find().sort('_id', -1).limit(10))
    for message in messages:
        message['_id'] = str(message['_id'])
    return messages

def increment_likes(message_id):
    try:
        result = messages_collection.update_one(
            {'_id': ObjectId(message_id)},
            {'$inc': {'likes': 1}}
        )
        if result.modified_count == 0:
            return {"error": "Message not found"}
        return {"message": "Message liked"}
    except Exception as e:
        return {"error": str(e)}