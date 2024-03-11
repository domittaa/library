import asyncio
import logging

import aio_pika
from aio_pika import ExchangeType
from aio_pika.abc import AbstractIncomingMessage


async def on_message(message: AbstractIncomingMessage):
    async with message.process():
        print(f"Message {message} received")


async def main(event_loop) -> None:
    logging.basicConfig(level=logging.DEBUG)

    connection_string = await aio_pika.connect_robust("amqp://guest:guest@127.0.0.1:5672/", loop=event_loop)

    channel = await connection_string.channel()

    await channel.set_qos(prefetch_count=10)

    exchange = await channel.declare_exchange("test", ExchangeType.FANOUT, durable=True)

    queue = await channel.declare_queue("test_queue", durable=True)

    second_queue = await channel.declare_queue("test_second_queue", durable=True)

    await queue.bind(exchange)
    await second_queue.bind(exchange)
    await queue.consume(on_message, timeout=60)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    connection = loop.run_until_complete(main(loop))

    loop.run_forever()
