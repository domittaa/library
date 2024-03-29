import asyncio
import logging
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.database import create_tables, sessionmanager
from message_broker.consumer import main as start_consuming
from source_code.api import authors, books, categories, orders, publishers
from source_code.config import settings

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG if settings.debug_logs else logging.INFO)


@asynccontextmanager  # converts function into async context manager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    """
    # before yield define what will be executed before app starts
    await create_tables()
    yield
    # after yield define what will be executed after app has finished
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan, title=settings.project_name, docs_url="/api/docs")

app.include_router(books.router, prefix="/books")
app.include_router(orders.router, prefix="/orders")
app.include_router(categories.router, prefix="/categories")
app.include_router(publishers.router, prefix="/publishers")
app.include_router(authors.router, prefix="/authors")
