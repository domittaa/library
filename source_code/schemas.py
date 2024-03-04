from datetime import date, datetime
from typing import List

from pydantic import BaseModel


class BookBase(BaseModel):

    title: str
    year: int
    is_loaned: bool
    category_id: int
    publisher_id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):

    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class BookSchema(BookBase):
    authors: List[AuthorBase]


class AuthorSchema(AuthorBase):
    books: List[BookBase]


class CategorySchema(BaseModel):

    name: str

    class Config:
        orm_mode = True


class PublisherSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: int
    address: str
    date_joined: date

    class Config:
        orm_mode = True


class NotificationSchema(BaseModel):
    text: str
    sent_at: datetime

    class Config:
        orm_mode = True
