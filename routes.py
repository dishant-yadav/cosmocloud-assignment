from fastapi import APIRouter
from schema import UserCreateSchema, UserResponseSchema
from crud import create_student

router = APIRouter()


@router.post("/students", response_model=UserResponseSchema, status_code=201)
def create_student_endpoint(student: UserCreateSchema):
    student_id = create_student(student.dict())
    return {"id": student_id, **student.dict()}
