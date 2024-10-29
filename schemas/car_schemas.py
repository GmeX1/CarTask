from pydantic import BaseModel, Field
from typing import Literal


class CarCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    brand: str = Field(min_length=1, max_length=255)
    price: float = Field(default=0)
    engine_type: Literal['diesel', 'electric', 'gasoline']


class CarReturn(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=255)
    brand: str = Field(min_length=1, max_length=255)
    price: float = Field(default=0)
    engine_type: Literal['diesel', 'electric', 'gasoline']
