from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.models import Author
from source_code.schemas import AuthorBase

router = APIRouter()


@router.post("/")
async def add_author(author: AuthorBase, db: AsyncSession = Depends(get_db_session)):
    author = Author(first_name=author.first_name, last_name=author.last_name)
    db.add(author)
    await db.commit()
    await db.refresh(author)
    return author
