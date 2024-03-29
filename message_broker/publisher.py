import asyncio

import aio_pika
from aio_pika import DeliveryMode, ExchangeType


async def send(message):
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@rabbitmq:5672/",
    )

    async with connection:

        channel = await connection.channel()

        exchange = await channel.declare_exchange("test", ExchangeType.FANOUT, durable=True)

        queue = await channel.declare_queue("test_queue", durable=True)
        second_queue = await channel.declare_queue("test_second_queue", durable=True)

        await queue.bind(exchange)
        await second_queue.bind(exchange)

        await exchange.publish(
            aio_pika.Message(body=message.encode(), delivery_mode=DeliveryMode.PERSISTENT),
            routing_key="test",
        )
