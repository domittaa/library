from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.models import Book, Category, Publisher
from source_code.schemas import BookBase, CategorySchema, PublisherSchema

router = APIRouter()


@router.get("/book/{book_id}")
async def get_book(book_id: int, db: AsyncSession = Depends(get_db_session)):
    book = (await db.scalars(select(Book).where(Book.id == book_id))).first()
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


@router.post("/publisher")
async def add_publisher(publisher: PublisherSchema, db: AsyncSession = Depends(get_db_session)):
    publisher = Publisher(name=publisher.name)
    db.add(publisher)
    await db.commit()
    await db.refresh(publisher)
    return publisher


@router.get("/publishers")
async def get_all_publishers(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Publisher))
    publishers = result.scalars().all()
    return {"publisher": publishers}


@router.post("/category")
async def add_category(category: CategorySchema, db: AsyncSession = Depends(get_db_session)):
    category = Category(name=category.name)
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category


@router.get("/categories")
async def get_all_categories(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Category))
    categories = result.scalars().all()
    return {"category": categories}
