from fastapi import (
    APIRouter,
    Query,
    HTTPException,
)
from schema import (
    UserCreateSchema,
    UserResponseSchema,
    ListStudentsResponse,
    UserUpdateSchema,
)
from crud import (
    create_student,
    list_students,
    fetch_student_by_id,
    update_student,
    delete_student,
)

router = APIRouter()


@router.post("/students", response_model=UserResponseSchema, status_code=201)
def create_student_endpoint(student: UserCreateSchema):
    student_id = create_student(student.dict())
    return {"id": student_id}


@router.get("/students", response_model=ListStudentsResponse, status_code=200)
def get_students(
    country: str = Query(default=None, description="Filter by country"),
    age: int = Query(default=None, description="Minimum age"),
):

    students = list_students(country=country, min_age=age)
    return {"data": students}


@router.get("/students/{id}", response_model=UserCreateSchema, status_code=200)
def get_student_endpoint(id: str):
    student = fetch_student_by_id(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.patch("/students/{id}", status_code=204)
def update_student_endpoint(id: str, student: UserUpdateSchema):
    updated = update_student(id, student.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found or not updated")
    return {"message": "Student updated successfully"}


@router.delete("/students/{id}", status_code=200)
def delete_student_endpoint(id: str):
    deleted = delete_student(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found or not deleted")
    return {"message": "Student deleted successfully"}
