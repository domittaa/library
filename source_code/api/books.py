from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from database.database import get_db_session
from database.models import Author, Book
from source_code.schemas import BookSchema, CreateBookSchema

router = APIRouter()


@router.get("/{book_id}", response_model=BookSchema)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Book).options(joinedload(Book.authors)).where(Book.id == book_id))
    book = result.unique().scalars().first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.get("/", response_model=list[BookSchema])
async def get_all_books(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Book).options(joinedload(Book.authors)))
    books = result.unique().scalars().all()
    return books


@router.post("/", response_model=BookSchema)
async def add_book(book: CreateBookSchema, db: AsyncSession = Depends(get_db_session)):
    new_book = Book(
        title=book.title,
        year=book.year,
        is_loaned=book.is_loaned,
        category_id=book.category_id,
        publisher_id=book.publisher_id,
    )
    if book.authors:
        author_query = select(Author).where(Author.id.in_(book.authors))
        result = await db.execute(author_query)
        authors = result.scalars().all()

        if len(authors) != len(book.authors):
            found_ids = {author.id for author in authors}
            missing_ids = set(book.authors) - found_ids
            raise HTTPException(status_code=404, detail=f"Authors with IDs {missing_ids} not found")

        new_book.authors = authors

    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    book_with_author = await db.execute(select(Book).options(joinedload(Book.authors)).where(Book.id == new_book.id))
    result = book_with_author.unique().scalars().first()
    return result
