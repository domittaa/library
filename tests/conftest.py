import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from database.database import Base
from source_code.config import settings


@pytest.fixture(scope="session")
async def engine():
    engine = create_async_engine(settings.test_database_url)
    yield engine
    await engine.dispose()


@pytest.fixture(scope="session")
async def tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def db_session(engine, tables):
    async_session = AsyncSession(engine)
    async with async_session as session:
        async with session.begin():
            yield session
