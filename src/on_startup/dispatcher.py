from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from src.handlers.basket.router import basket_router
from src.handlers.catigories.router import categories_router
# from src.handlers.admin.router import admin_router
from src.handlers.menu.customer.router import customer_router
from src.handlers.menu.deliverer.router import delivery_router
from src.handlers.main.router import main_router
from src.handlers.products.router import products_router
from src.integrations.redis import redis
from src.middleware.auth import AuthMiddleware
from src.middleware.logger import LogMessageMiddleware


def setup_dispatcher(bot: Bot) -> Dispatcher:
    storage = RedisStorage(redis)
    dp = Dispatcher(storage=storage, bot=bot)

    dp.include_routers(main_router)
    dp.include_routers(customer_router)
    dp.include_routers(products_router)
    dp.include_routers(categories_router)
    dp.include_routers(delivery_router)
    dp.include_routers(basket_router)

    dp.message.middleware(LogMessageMiddleware())
    dp.callback_query.middleware(LogMessageMiddleware())

    dp.message.middleware(AuthMiddleware())
    dp.callback_query.middleware(AuthMiddleware())

    return dp