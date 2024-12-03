from pydantic import BaseModel


class AddressSchema(BaseModel):
    city: str
    country: str


class UserCreateSchema(BaseModel):
    name: str
    age: int
    address: AddressSchema


class UserResponseSchema(UserCreateSchema):
    id: str
