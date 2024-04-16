import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_db_session
from database.models import Order
from message_broker.publisher import send
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
    order = Order(date=order.date, due_date=order.due_date, user_id=order.user_id)
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order


@router.post("/find_expired_today")
async def find_expired_orders(db: AsyncSession = Depends(get_db_session)):
    results = await db.execute(select(Order).where(Order.due_date == datetime.date.today()))
    order = results.scalars().all()
    if order:
        for order in order:
            text = f"Your order expires today."
            message = f"Your order {order} expires today"
            # notification = Notification(text=text, sent_at=datetime.datetime.now(), order_id=order.id)
            # db.add(notification)
            # await db.commit()
            # await db.refresh(notification)
            await send(message)
    return "message send"
