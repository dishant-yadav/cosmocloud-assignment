from pydantic import BaseModel
from typing import List


class AddressSchema(BaseModel):
    city: str
    country: str


class UserCreateSchema(BaseModel):
    name: str
    age: int
    address: AddressSchema


class UserResponseSchema(UserCreateSchema):
    id: str


class Student(BaseModel):
    name: str
    age: int


class ListStudentsResponse(BaseModel):
    data: List[Student]
