from database.models import async_session
from database.models import Client
from sqlalchemy import select, update, delete, desc
import asyncio


async def get_free_app():
    async with async_session() as session:
        free_app = await session.scalars(select(Client).where(Client.booking == 0))
        return free_app

#asyncio.run(get_free_app())
