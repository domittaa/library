import logging
import sys
from contextlib import asynccontextmanager

from source_code.config import settings
from source_code.database import sessionmanager
from fastapi import FastAPI

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG if settings.debug_logs else logging.INFO)


@asynccontextmanager  # converts function into async context manager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    """
    # before yield define what will be executed before app starts
    yield
    # after yield define what will be executed after app has finished
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan, title=settings.project_name, docs_url="/api/docs")


@app.get("/")
async def root():
    return {"message": "Hello World"}


