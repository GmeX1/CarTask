from pydantic import BaseModel, Field
from typing import List
from schemas.order_schemas import OrderReturn


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)


class UserReturn(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=255)
    orders: List[OrderReturn] = None


class UserEdit(UserCreate):
    pass
