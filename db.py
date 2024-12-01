from pymongo import MongoClient
import os

uri = os.getenv("MONGODBURI")

client = MongoClient(uri)
db = client.get_database("student_management")
student_collection = db.get_collection("students")
