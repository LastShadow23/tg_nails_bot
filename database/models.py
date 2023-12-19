from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import asyncio

from datetime import datetime


sqlite_database = "sqlite+aiosqlite:///clients.db"

engine = create_async_engine(sqlite_database, echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Schedule(Base):
    __tablename__ = "schedule"

    date: Mapped[DateTime] = mapped_column(DateTime, unique=True, primary_key=True)
    is_work: Mapped[Boolean] = mapped_column(Boolean, default=True)
    is_book: Mapped[Boolean] = mapped_column(Boolean, default=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="dates")

    def __repr__(self):
        return f"[Дата: {self.date}, Рабочий день: {self.is_work}, Предоплата: {self.is_book}, " \
               f"Клиент: {self.customer_id}]"


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    tg_id: Mapped[int] = mapped_column(Integer)
    phone: Mapped[str] = mapped_column(String(30))
    dates: Mapped["Schedule"] = relationship(back_populates="customer")

    def __repr__(self):
        return f"Клиент [ID: {self.id}, Имя: {self.name}, TG ID: {self.tg_id}, Телефон: {self.phone}]"


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(async_main())
