import asyncio
import logging

import aio_pika
from aio_pika import ExchangeType
from aio_pika.abc import AbstractIncomingMessage


async def on_message(message: AbstractIncomingMessage):
    print("on message")
    async with message.process():
        print(f"Message {message} received")


async def main(event_loop) -> None:
    logging.basicConfig(level=logging.DEBUG)
    connection = await aio_pika.connect_robust("amqp://guest:guest@127.0.0.1:5672/", loop=event_loop)

    queue_name = "notification_queue"

    # channel = await connection.channel()

    # queue = await channel.declare_queue(queue_name, auto_delete=True)

    channel = await connection.channel()
    await channel.set_qos(prefetch_count=10)
    exchange = await channel.declare_exchange("test", ExchangeType.FANOUT, durable=True)
    queue = await channel.declare_queue("test_queue", durable=True)
    second_queue = await channel.declare_queue("test_second_queue", durable=True)
    await queue.bind(exchange)
    await second_queue.bind(exchange)

    await queue.consume(on_message, timeout=60)
    print("test")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    connection = loop.run_until_complete(main(loop))

    loop.run_forever()
    # finally:
    #     loop.run_until_complete(connection.cancel())
