from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.models import Publisher
from source_code.schemas import PublisherSchema

router = APIRouter()


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
