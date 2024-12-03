from bson import ObjectId
from db import database

students_collection = database["students"]


def create_student(student: dict) -> str:
    result = students_collection.insert_one(student)
    return str(result.inserted_id)


def list_students(country: str = None, min_age: int = None) -> list:
    query = {}
    if country:
        query["address.country"] = country
    if min_age:
        query["age"] = {"$gte": min_age}

    students = students_collection.find(query)
    return [student for student in students]
