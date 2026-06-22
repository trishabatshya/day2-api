from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()


class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    settings.database_url,
    echo=True,  # logs every SQL query — useful while learning, remove in production
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session