from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.models import Book
from source_code.schemas import BookBase

router = APIRouter()


@router.get("/book/{book_id}")
async def get_book(book_id: int, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalars().first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.get("/books")
async def get_all_books(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Book))
    books = result.scalars().all()
    return {"books": books}


@router.post("/book")
async def add_book(book: BookBase, db: AsyncSession = Depends(get_db_session)):
    book = Book(title=book.title, year=book.year, is_loaned=book.is_loaned)
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return book
