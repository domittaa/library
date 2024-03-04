import datetime

from sqlalchemy import select

from database.database import get_db_session
from database.models import Notification, Order


async def find_expire_today():
    db = get_db_session()
    results = await db.execute(select(Order).where(Order.due_date == datetime.date.today()))
    order = results.scalars().all()
    for order in order:
        text = "Your order expires today."
        notification = Notification(text=text, sent_at=datetime.datetime.now(), order_id=order.id)
        await db.commit()
        await db.refresh(notification)
        # put on queue