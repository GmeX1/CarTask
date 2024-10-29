from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)


class UserReturn(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=255)
