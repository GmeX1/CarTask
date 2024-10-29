from pydantic import BaseModel, Field
from datetime import datetime


class OrderCreate(BaseModel):  # Добавить кастомные валидаторы через @field_validator('name')
    user_id: int
    car_id: int


class OrderReturn(BaseModel):
    id: int
    creation_date: datetime
    user_id: int
    car_id: int
