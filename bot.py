import asyncio
from aiogram import Bot, Dispatcher
from handlers.handlers import router
from dotenv import load_dotenv
import os


load_dotenv()


async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

