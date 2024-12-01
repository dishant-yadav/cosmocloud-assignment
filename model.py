from pydantic import BaseModel, Field
from typing import Optional


class Address(BaseModel):
    city: str
    country: str


class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    age: int
    address: Address
