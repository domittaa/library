import datetime
import time

import aio_pika
from aio_pika import DeliveryMode, ExchangeType
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.models import Author, Book
from source_code.schemas import AuthorBase, BookBase, BookSchema

router = APIRouter()


@router.get("/publish")
async def send():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@rabbitmq:5672/",
    )

    async with connection:
        routing_key = ""

        channel = await connection.channel()
        exchange = await channel.declare_exchange("test", ExchangeType.FANOUT, durable=True)
        queue = await channel.declare_queue("test_queue", durable=True)
        second_queue = await channel.declare_queue("test_second_queue", durable=True)
        await queue.bind(exchange)
        await second_queue.bind(exchange)

        print("sending message")
        await exchange.publish(
            aio_pika.Message(body=f"Hello {routing_key}".encode(), delivery_mode=DeliveryMode.PERSISTENT),
            routing_key="test",
        )
        print("message send")


@router.get("/{book_id}")
async def get_book(book_id: int, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalars().first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.get("/")
async def get_all_books(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Book))
    books = result.scalars().all()
    return {"books": books}


@router.post("/")
async def add_book(book: BookSchema, db: AsyncSession = Depends(get_db_session)):
    book = Book(title=book.title, year=book.year, is_loaned=book.is_loaned)
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book


@router.post("/author")
async def add_author(author: AuthorBase, db: AsyncSession = Depends(get_db_session)):
    author = Author(first_name=author.first_name, last_name=author.last_name)
    db.add(author)
    await db.commit()
    await db.refresh(author)
    return author
