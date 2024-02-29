import logging
import sys
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import create_tables, get_db_session, sessionmanager
from database.models import Book
from source_code.config import settings
from source_code.schemas import BookBase

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG if settings.debug_logs else logging.INFO)


@asynccontextmanager  # converts function into async context manager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    """
    # before yield define what will be executed before app starts
    await create_tables()

    yield
    # after yield define what will be executed after app has finished
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan, title=settings.project_name, docs_url="/api/docs")


@app.get("/book/{book_id}")
async def get_book(book_id: int, db: AsyncSession = Depends(get_db_session)):
    book = (await db.scalars(select(Book).where(Book.id == book_id))).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.get("/book")
async def get_books(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Book))
    books = result.scalars().all()
    return {"books": books}


@app.post("/book")
async def add_book(book: BookBase, db: AsyncSession = Depends(get_db_session)):
    book = Book(title=book.title, year=book.year, is_loaned=book.is_loaned)
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book
