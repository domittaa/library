import asyncio

import aio_pika
from aio_pika import DeliveryMode, ExchangeType


async def main() -> None:
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@rabbitmq:5672/",
    )

    async with connection:
        routing_key = ""

        channel = await connection.channel()
        exchange = await channel.declare_exchange("test", ExchangeType.FANOUT, durable=True)
        queue = await channel.declare_queue("test_queue", durable=True)
        second_queue = await channel.declare_queue("test_second_queue", durable=True)
        await queue.bind(exchange)
        await second_queue.bind(exchange)

        print("sending message")
        await exchange.publish(
            aio_pika.Message(body=f"Hello {routing_key}".encode(), delivery_mode=DeliveryMode.PERSISTENT),
            routing_key="test",
        )
        print("message send")


if __name__ == "__main__":
    asyncio.run(main())
