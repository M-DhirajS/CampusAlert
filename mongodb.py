import os
from pymongo import MongoClient

# Read the MongoDB connection string from an environment variable (set in Render)
# Fallback to the local development URI if not set.
MONGO_URI = os.environ.get(
    "MONGODB_URI",
    "mongodb+srv://Dhiraj:root@cluster0.b51rrue.mongodb.net/?retryWrites=true&w=majority"
)

client = MongoClient(MONGO_URI)

db = client["CampusAlertDB"]

users = db["users"]
