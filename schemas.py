from datetime import datetime
from pydantic import BaseModel, Field


class UserPublic(BaseModel):
    id: int
    username: str
    age: int | None = None
    created_at: datetime

    class Config:
        from_attributes = True


class UserRegister(BaseModel):
    username: str = Field(min_length=3, max_length=64)
    password: str = Field(min_length=6, max_length=128)
    age: int | None = Field(default=None, ge=0, le=150)


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class PostCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    body: str = Field(min_length=1)


class PostResponse(BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime
    author: UserPublic

    class Config:
        from_attributes = True