from datetime import date, datetime
from typing import List

from pydantic import BaseModel


class BookBase(BaseModel):

    id: int
    title: str
    year: int
    is_loaned: bool
    category_id: int
    publisher_id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):

    id: int
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class BookSchema(BookBase):
    authors: List[AuthorBase]


class AuthorSchema(AuthorBase):
    books: List[BookBase]


class Category(BaseModel):

    id: int
    name: str

    class Config:
        orm_mode = True


class Publisher(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: int
    address: str
    date_joined: date

    class Config:
        orm_mode = True


class Notification(BaseModel):
    id: int
    text: str
    sent_at: datetime

    class Config:
        orm_mode = True
