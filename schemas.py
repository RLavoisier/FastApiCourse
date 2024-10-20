import uuid
from typing import List

from pydantic import BaseModel


class Article(BaseModel):
    id: uuid.UUID
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    id: uuid.UUID
    articles: List[Article]

    class Config:
        orm_mode = True


class User(BaseModel):
    id: uuid.UUID
    username: str
    email: str

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    user_id: uuid.UUID


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        orm_mode = True
