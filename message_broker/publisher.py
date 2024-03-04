import asyncio

import aio_pika


async def main() -> None:
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/",
    )

    async with connection:
        routing_key = "notification_queue"

        channel = await connection.channel()

        print("sending message")
        await channel.default_exchange.publish(
            aio_pika.Message(body=f"Hello {routing_key}".encode()),
            routing_key=routing_key,
        )
        print("message send")


if __name__ == "__main__":
    asyncio.run(main())
