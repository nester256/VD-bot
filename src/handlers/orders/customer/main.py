from aiogram import F, types

from src.buttons.menu.customer.config import SHOW_ORDERS_CALLBACK
from src.buttons.orders.customer.getter import get_orders_button
from src.handlers.orders.customer.router import orders_router
from src.logger import logger
from src.requests.orders.orders import get_orders
from src.template.render import render

from conf.config import settings


@orders_router.callback_query(F.data == SHOW_ORDERS_CALLBACK)
async def menu_orders_callback_handler(callback: types.CallbackQuery) -> None:
    try:
        await callback.message.delete()
        orders = await get_orders()
        await callback.message.answer(
            text=render(
                'orders/info.jinja2',
                active_orders=[order for order in orders if order['status'] != 'done'],
                complete_orders=[order for order in orders if order['status'] == 'done'],
            ),
            parse_mode='HTML',
            reply_markup=get_orders_button(),
        )
    except Exception as err:
        await callback.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при выводе заказов: {err}')
