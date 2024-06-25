from aiogram import types
from aiogram.fsm.context import FSMContext

from src.buttons.categories.config import ProductCallback
from src.buttons.products.config import ProductPaginationCallback
from src.buttons.products.getter import get_products_buttons
from src.handlers.products.router import products_router
from src.logger import logger
from src.requests.products.products import get_products
from src.template.render import render

from conf.config import settings


@products_router.callback_query(ProductCallback.filter())
async def products_callback_handler(
    callback: types.CallbackQuery, callback_data: ProductCallback, state: FSMContext
) -> None:
    cat_id = int(callback_data.id)
    try:
        await callback.message.delete()
        products = await get_products(0, cat_id)
        await state.set_state(None)
        if not products:
            await callback.message.answer(settings.NOTHING_ERROR_MSG)
        await callback.message.answer_photo(
            photo=settings.CATEGORIES_PHOTO,
            caption=render(
                'products/prod_msg.jinja2',
            ),
            parse_mode='HTML',
            reply_markup=get_products_buttons(products, cat_id),
        )
    except Exception as err:
        await callback.message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при получении товаров: {err}')


@products_router.callback_query(ProductPaginationCallback.filter())
async def handle_pagination_products(
    callback: types.CallbackQuery, callback_data: ProductPaginationCallback, state: FSMContext
):
    offset = int(callback_data.offset)
    cat_id = int(callback_data.c_id)
    try:
        await callback.message.delete()
        products = await get_products(offset, cat_id)
        if not products:
            offset = 0
            products = await get_products(0, cat_id)
        await callback.message.answer_photo(
            photo=settings.CATEGORIES_PHOTO,
            caption=render(
                'products/prod_msg.jinja2',
            ),
            parse_mode='HTML',
            reply_markup=get_products_buttons(products, cat_id, offset),
        )
    except Exception as err:
        await callback.message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при получении категорий: {err}')
