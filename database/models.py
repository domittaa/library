from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


class BookAuthor(Base):
    __tablename__ = "book_author"
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    author_id = Column(Integer, ForeignKey("authors.id"), primary_key=True)


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, unique=True, nullable=False)
    year = Column(Integer)
    is_loaned = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    publisher_id = Column(Integer, ForeignKey("publishers.id"))

    category = relationship("Category", back_populates="books")
    publisher = relationship("Publisher", back_populates="books")
    authors = relationship("Author", secondary=BookAuthor, back_populates="books")


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)

    books = relationship("Book", secondary=BookAuthor, back_populates="authors")


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)

    books = relationship("Book", back_populates="category")


class Publisher(Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)

    books = relationship("Book", back_populates="publisher")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(Integer)
    address = Column(String)
    date_joined = Column(Date)

    orders = relationship("Order", back_populates="user")


# class Order(Base):
#     __tablename__ = "orders"
#     id = Column(Integer, primary_key=True, autoincrement=True, index=True)
#     date = Column(Date, nullable=False)
#     due_date = Column(Date)
#     extension = Column(Boolean, default=False)
#     is_returned = Column(Boolean, default=False)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     book_id = Column(Integer, ForeignKey("books.id"))
#
#     books = relationship("Book", back_populates="category")


class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    text = Column(String, nullable=False)
    sent_at = Column(DateTime)
    # order_id = Column(Integer, ForeignKey("orders.id"))
