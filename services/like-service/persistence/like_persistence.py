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
    # Increment the likes count for the specified message in the messages collection
    result = list(messages_collection.find(
        {"_id": ObjectId(message_id)}
    ))
    
    print(result)
    
    # Check if the message was found and updated
    # if result.modified_count == 1:
    #     return True
    # else:
    #     return False

def fetch_latest_messages():
    messages = list(likes_collection.find().sort('_id', -1).limit(10))
    for message in messages:
        message['_id'] = str(message['_id'])
    return messages