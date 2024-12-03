from bson import ObjectId
from db import database
from fastapi import HTTPException

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


def fetch_student_by_id(student_id: str) -> object:
    try:
        obj_id = ObjectId(student_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format.")

    student = students_collection.find_one({"_id": obj_id})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    return student


def update_student(student_id: str, update_data: dict) -> object:
    result = students_collection.update_one(
        {"_id": ObjectId(student_id)}, {"$set": update_data}
    )
    return result.modified_count > 0


def delete_student(student_id: str) -> object:
    result = students_collection.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0
