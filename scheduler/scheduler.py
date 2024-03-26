import asyncio
import datetime

from sqlalchemy import select

from database.database import get_db_session
from database.models import Notification, Order
from message_broker.publisher import send


async def find_expire_today():
    db = get_db_session()
    results = await db.execute(select(Order).where(Order.due_date == datetime.date.today()))
    order = results.scalars().all()
    for order in order:
        text = f"Your order expires today."
        message = {
            "order_id": order.id,
            "message": text
        }
        notification = Notification(text=text, sent_at=datetime.datetime.now(), order_id=order.id)
        await db.commit()
        await db.refresh(notification)
        asyncio.run(send(message))


if __name__ == "__main__":
    asyncio.run(find_expire_today())
