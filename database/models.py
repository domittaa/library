from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from database.database import Base

order_book_association = Table(
    "order_book",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("order.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
)


book_author = Table(
    "book_author",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("book.id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("author.id"), primary_key=True),
)


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    year = Column(Integer)
    is_loaned = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey("category.id"))
    publisher_id = Column(Integer, ForeignKey("publisher.id"))

    category = relationship("Category", back_populates="book")
    publisher = relationship("Publisher", back_populates="book")
    authors = relationship("Author", secondary=book_author, back_populates="books")
    orders = relationship("Order", secondary=order_book_association, back_populates="books")


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)

    books = relationship("Book", secondary=book_author, back_populates="authors")


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    book = relationship("Book", back_populates="category")


class Publisher(Base):
    __tablename__ = "publisher"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    book = relationship("Book", back_populates="publisher")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(Integer, unique=True)
    address = Column(String)
    date_joined = Column(Date)

    order = relationship("Order", back_populates="user")


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    due_date = Column(Date)
    extension = Column(Boolean, default=False)
    is_returned = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="order")
    books = relationship("Book", secondary=order_book_association, back_populates="orders")
    notification = relationship("Notification", back_populates="order")


class Notification(Base):  # not sure if store in db
    __tablename__ = "notification"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    sent_at = Column(DateTime)
    order_id = Column(Integer, ForeignKey("order.id"))

    order = relationship("Order", back_populates="notification")
