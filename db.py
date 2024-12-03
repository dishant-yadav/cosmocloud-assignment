from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGODBURI_LOCAL")
DB_NAME = os.getenv("DB_NAME", "student_management")

client = MongoClient(MONGO_URL)
db = client.get_database(DB_NAME)
