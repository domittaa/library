from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.models import User
from source_code.schemas import CreateUserSchema, UserSchema

router = APIRouter()


@router.post("/", response_model=UserSchema)
async def add_user(user: CreateUserSchema, db: AsyncSession = Depends(get_db_session)):
    user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone=user.phone,
        address=user.address,
        date_joined=user.date_joined,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


@router.get("/", response_model=list[UserSchema])
async def get_all_users(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User).order_by(User.id))
    users = result.scalars().all()
    return users
