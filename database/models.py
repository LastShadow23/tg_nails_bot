from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import Integer, String, Boolean, DateTime

from datetime import datetime


sqlite_database = "sqlite:///clients.db"

engine = create_async_engine(sqlite_database)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    date = mapped_column(DateTime)
    time: Mapped[str] = mapped_column(String(10))
    name: Mapped[str] = mapped_column(String(30))
    booking: Mapped[Boolean] = mapped_column(Boolean)
    tg_id: Mapped[int] = mapped_column(Integer)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
