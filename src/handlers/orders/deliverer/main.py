from aiogram import F, types

from src.buttons.menu.deliverer.config import SHOW_ACTIVE_ORDERS, SHOW_AWAITING_ORDERS
from src.buttons.orders.deliverer.config import SetDeliverer, SetDone
from src.buttons.orders.deliverer.getter import get_active_deliverer_button, get_orders_deliverer_button
from src.handlers.orders.deliverer.router import orders_deliverer_router
from src.logger import logger
from src.requests.orders.orders import create_delivery, get_active, get_awaiting_orders, set_done
from src.template.render import render

from conf.config import settings


@orders_deliverer_router.callback_query(F.data == SHOW_AWAITING_ORDERS)
async def orders_awaiting_callback_handler(callback: types.CallbackQuery) -> None:
    try:
        await callback.message.delete()
        orders = await get_awaiting_orders()
        if orders:
            await callback.message.answer(
                text=render('orders/delivery_info.jinja2', orders=orders),
                parse_mode='HTML',
                reply_markup=get_orders_deliverer_button(orders),
            )
        else:
            await callback.message.answer(text='Нет доступных заказов для доставки')
    except Exception as err:
        await callback.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при выводе заказов: {err}')


@orders_deliverer_router.callback_query(SetDeliverer.filter())
async def set_deliverer_callback_handler(callback: types.CallbackQuery, callback_data: SetDeliverer) -> None:
    order_id = callback_data.order_id
    try:
        res = await create_delivery(order_id)
        if res:
            await callback.message.answer(text='Успешное добавление заказа в активные!')
        else:
            await callback.message.answer(text='Ошибка при добавлении заказа в активные!')
    except Exception as err:
        await callback.message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при добавлении заказа в активные: {err}')


@orders_deliverer_router.callback_query(F.data == SHOW_ACTIVE_ORDERS)
async def orders_active_callback_handler(callback: types.CallbackQuery) -> None:
    try:
        await callback.message.delete()
        orders = await get_active()
        if orders:
            await callback.message.answer(
                text=render('orders/delivery_info.jinja2', orders=orders),
                parse_mode='HTML',
                reply_markup=get_active_deliverer_button(orders),
            )
        else:
            await callback.message.answer(text='Нет активных заказов')
    except Exception as err:
        await callback.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при выводе заказов: {err}')


@orders_deliverer_router.callback_query(SetDone.filter())
async def set_done_callback_handler(callback: types.CallbackQuery, callback_data: SetDone) -> None:
    order_id = callback_data.order_id
    try:
        res = await set_done(order_id)
        if res:
            await callback.message.answer(text='Успешное обновление статуса - выполнен!')
        else:
            await callback.message.answer(text='Ошибка при обновление статуса - попробуйте еще раз!')
    except Exception as err:
        await callback.message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при обновление статуса: {err}')
