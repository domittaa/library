from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.models import Category
from source_code.schemas import CategorySchema

router = APIRouter()


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
