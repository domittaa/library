import logging

import aio_pika
from aio_pika import ExchangeType
from aio_pika.abc import AbstractIncomingMessage

from notifications.send_notification import send_email


async def on_message(message: AbstractIncomingMessage):
    async with message.process():
        send_email(message.body.decode())
        return message


async def start_consumer(event_loop) -> None:
    logging.basicConfig(level=logging.DEBUG)

    connection_string = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq:5672/", loop=event_loop)

    channel = await connection_string.channel()

    await channel.set_qos(prefetch_count=10)

    exchange = await channel.declare_exchange("test", ExchangeType.FANOUT, durable=True)

    queue = await channel.declare_queue("test_queue", durable=True)

    second_queue = await channel.declare_queue("test_second_queue", durable=True)

    await queue.bind(exchange)
    await second_queue.bind(exchange)
    await queue.consume(on_message, timeout=60)
