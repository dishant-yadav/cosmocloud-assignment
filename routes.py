from fastapi import APIRouter, Query
from schema import UserCreateSchema, UserResponseSchema, ListStudentsResponse
from crud import create_student, list_students

router = APIRouter()


@router.post("/students", response_model=UserResponseSchema, status_code=201)
def create_student_endpoint(student: UserCreateSchema):
    student_id = create_student(student.dict())
    return {"id": student_id, **student.dict()}


@router.get("/students", response_model=ListStudentsResponse)
def get_students(
    country: str = Query(default=None, description="Filter by country"),
    age: int = Query(default=None, description="Minimum age"),
):

    students = list_students(country=country, min_age=age)
    return {"data": students}
