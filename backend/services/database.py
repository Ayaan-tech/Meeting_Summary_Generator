from pymongo import MongoClient
from pymongo.mongo_client import MongoClient

MONGO_URI = "mongodb+srv://khanramsha302020:Gal7FcruiV8WC6Du@cluster0.bkluy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" 

client = MongoClient(MONGO_URI,tls = True)

db = client["meeting_details"]
collection = db["meeting"]

def save_meeting_data(meeting_data: dict):
    try:
        collection.insert_one(meeting_data)
        print("Meeting details successfully saved to MongoDB.")
    except Exception as e:
        print(f"Error saving meeting details to MongoDB: {e}")
