from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class OrderCreate(BaseModel):  # Добавить кастомные валидаторы через @field_validator('name')
    user_id: int
    car_id: int


class OrderReturn(BaseModel):
    id: int
    creation_date: datetime
    user_id: int
    car_id: int


class OrderEdit(BaseModel):
    creation_date: Optional[datetime] = None
    user_id: Optional[int] = None
    car_id: Optional[int] = None

