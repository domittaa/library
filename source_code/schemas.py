from datetime import date, datetime
from typing import List

from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class BookBase(BaseModel):

    title: str
    year: int
    is_loaned: bool = False
    category_id: int
    publisher_id: int

    class Config:
        orm_mode = True  # read the data even if it is not a dict, but an ORM model


class BookSchema(BookBase):
    id: int
    authors: list[AuthorBase]


class CreateBookSchema(BookBase):
    authors: list[int]


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


class OrderSchema(BaseModel):
    date: date
    due_date: date
    extension: bool = False
    is_returned: bool = False
    user_id: int
    books: List[int]

    class Config:
        orm_mode = True
