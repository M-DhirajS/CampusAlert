from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Dhiraj:root@cluster0.b51rrue.mongodb.net/?retryWrites=true&w=majority"
)

db = client["CampusAlertDB"]

users = db["users"]