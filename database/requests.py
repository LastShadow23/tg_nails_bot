from database.models import Schedule, Customer, async_session
from sqlalchemy import select, update, delete, desc
from datetime import datetime, date, time, timedelta
from calendar import monthrange
import asyncio


# генерация расписания на следующий месяц

async def make_schedule():
    async with async_session() as session:
        t1 = time(11, 00)
        t2 = time(17, 00)

        next_month_day = (datetime.now().replace(day=1) + timedelta(days=31)).replace(day=1)
        next_month = next_month_day.month
        year = next_month_day.year

        for num_day in range(1, monthrange(year, next_month)[1] + 1):
            t1_date = datetime.combine(date(year, next_month, num_day), t1)
            t2_date = datetime.combine(date(year, next_month, num_day), t2)

            if await session.get(Schedule, t1_date):
                return

            session.add(Schedule(date=t1_date, is_work=t1_date.isoweekday() not in (3, 6)))
            session.add(Schedule(date=t2_date, is_work=t1_date.isoweekday() not in (3, 6)))

        await session.commit()


async def get_free_records():
    async with async_session() as session:
        result = await session.scalars(select(Schedule.date).where(Schedule.is_work == 1).where
                                       (Schedule.date >= datetime.now()).where
                                       (Schedule.customer_id.is_(None)))
        return result

# async def get_free_app():
#     async with async_session() as session:
#         free_app = await session.scalars(select(Schedule.date).where(Schedule.is_work == 1).where
#                                          (Schedule.date >= datetime.now()).where
#                                          (Schedule.customer_id.is_(None)))
#         return free_app


# asyncio.run(get_free_app())
