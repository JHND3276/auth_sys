from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config.settings import Config

Base = declarative_base()

from src.auth.models import User

engine = create_async_engine(Config.DATABASE_URL, echo = Config.DEBUG)
AsyncSessionLocal = sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session