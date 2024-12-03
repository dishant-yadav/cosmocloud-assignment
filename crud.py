from bson import ObjectId
from db import database

students_collection = database["students"]

def create_student(student: dict):
    result = students_collection.insert_one(student)
    return str(result.inserted_id)
