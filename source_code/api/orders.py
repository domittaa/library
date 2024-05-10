import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from database.database import get_db_session
from database.models import Book, Order
from message_broker.publisher import send
from source_code.schemas import CreateOrderSchema, OrderSchema

router = APIRouter()


@router.get("/", response_model=list[OrderSchema])
async def get_all_orders(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(
        select(Order).options(joinedload(Order.books).joinedload(Book.authors)).order_by(Order.id)
    )
    orders = result.unique().scalars().all()
    return orders


@router.get("/{order_id}", response_model=OrderSchema)
async def get_order(order_id: int, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(
        select(Order).options(joinedload(Order.books).joinedload(Book.authors)).where(Order.id == order_id)
    )
    order = result.unique().scalars().first()
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with id {order_id} does not exists")
    return order


@router.post("/", response_model=OrderSchema)
async def create_order(order: CreateOrderSchema, db: AsyncSession = Depends(get_db_session)):
    new_order = Order(
        date=order.date,
        due_date=order.due_date,
        extension=order.extension,
        is_returned=order.is_returned,
        user_id=order.user_id,
    )

    book_query = select(Book).where(Book.id.in_(order.books))
    result = await db.execute(book_query)
    books = result.scalars().all()

    if len(books) != len(order.books):
        found_ids = {book.id for book in books}
        missing_ids = set(order.books) - found_ids
        raise HTTPException(status_code=404, detail=f"Books with IDs {missing_ids} not found")

    new_order.books = books

    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    order_with_books = await db.execute(
        select(Order).options(joinedload(Order.books).joinedload(Book.authors)).where(Order.id == new_order.id)
    )
    result = order_with_books.unique().scalars().first()
    return result


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
