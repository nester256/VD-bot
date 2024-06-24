from aiogram import types, F
from aiogram.fsm.context import FSMContext

from conf.config import settings
from src.buttons.menu.customer.config import SHOW_BASKET_CALLBACK
from src.buttons.product.config import AddToBasketCallback, RemoveBasketCallback, CREATE_ORDER_CALLBACK
from src.handlers.basket.cart import add_to_cart, get_cart, send_cart_buttons, remove_from_cart, get_cart_summary, \
    clear_cart
from src.handlers.basket.router import basket_router
from src.logger import logger
from src.requests.basket.basket import send_basket


@basket_router.callback_query(AddToBasketCallback.filter())
async def basket_add_callback_handler(callback: types.CallbackQuery, callback_data: AddToBasketCallback) -> None:
    product = {
        "id": callback_data.id,
        "name": callback_data.name,
        "price": callback_data.price
    }
    try:
        user_id = callback.from_user.id
        await add_to_cart(user_id, product)
        await callback.message.answer(text=f"Успешное добавление товара в корзину!")
    except Exception as err:
        await callback.message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при добавлении товара в корзину: {err}')


@basket_router.callback_query(F.data == SHOW_BASKET_CALLBACK)
async def basket_show_callback_handler(callback: types.CallbackQuery) -> None:
    user_id = callback.from_user.id
    cart = await get_cart(user_id)
    await send_cart_buttons(cart, callback)


@basket_router.callback_query(RemoveBasketCallback.filter())
async def basket_remove_callback_handler(callback: types.CallbackQuery, callback_data: RemoveBasketCallback) -> None:
    product_id = callback_data.id
    await callback.message.delete()
    try:
        user_id = callback.from_user.id
        await remove_from_cart(user_id, product_id)
        cart = await get_cart(user_id)
        await send_cart_buttons(cart, callback)
        await callback.message.answer(text=f"Успешное удаление товара из корзины!")
    except Exception as err:
        await callback.message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при удалении товара из корзины: {err}')


@basket_router.callback_query(F.data == CREATE_ORDER_CALLBACK)
async def create_order_callback_handler(callback: types.CallbackQuery) -> None:
    await callback.message.delete()
    try:
        user_id = callback.from_user.id
        basket_info = await get_cart_summary(user_id)
        res = await send_basket(basket_info)
        print(basket_info)
        if not res:
            await callback.message.answer(settings.DEFAULT_ERROR_MSG)
            logger.error(f'Ошибка при создании заказа - ошибка бэка')
        else:
            await clear_cart(user_id)
            await callback.message.answer(text=f"Заказ успешно создан!")
    except Exception as err:
        await callback.message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при создании заказа: {err}')
