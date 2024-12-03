from pydantic import BaseModel, Field
from typing import List, Optional


class AddressSchema(BaseModel):
    city: str
    country: str


class AddressUpdateSchema(BaseModel):
    city: Optional[str] = Field(None)
    country: Optional[str] = Field(None)


class UserCreateSchema(BaseModel):
    name: str
    age: int
    address: AddressSchema


class UserResponseSchema(BaseModel):
    id: str


class Student(BaseModel):
    name: str
    age: int


class ListStudentsResponse(BaseModel):
    data: List[Student]


class UserUpdateSchema(BaseModel):
    name: Optional[str] = Field(None)
    age: Optional[int] = Field(None, ge=0)
    address: Optional[AddressUpdateSchema] = Field(None)
