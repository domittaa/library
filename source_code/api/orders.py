from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.models import Order
from source_code.schemas import OrderSchema

router = APIRouter()


@router.get("/")
async def get_all_orders(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Order))
    orders = result.scalars().all()
    return {"orders": orders}


@router.get("/{order_id}")
async def get_order(order_id: int, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalars().first()
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with id {order_id} does not exists")
    return order


@router.post("/")
async def create_order(order: OrderSchema, db: AsyncSession = Depends(get_db_session)):
    order = Order(user=order.user_id, date=order.date, due_date=order.due_date)
    await db.commit()
    await db.refresh(order)
    return order
