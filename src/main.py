import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis

from conf.config import settings
from src.handlers.login.router import login_router
from src.handlers.main.router import main_router
from src.handlers.products.router import products_router


logging.basicConfig(level=logging.INFO)
print(settings.BOT_TOKEN)
bot = Bot(token=settings.BOT_TOKEN)

redis = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
)

storage = RedisStorage(redis)
dp = Dispatcher(storage=storage)

dp.include_routers(main_router)
dp.include_routers(login_router)
dp.include_routers(products_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
