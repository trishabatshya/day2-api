from pydantic import BaseModel, EmailStr
from typing import Optional


# --- Auth schemas ---

class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# --- User schemas ---

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = {"from_attributes": True}


# --- Post schemas ---

class PostCreate(BaseModel):
    title: str
    content: str
    price: float


class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    price: float | None = None


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    price: float
    author_id: int

    model_config = {"from_attributes": True}