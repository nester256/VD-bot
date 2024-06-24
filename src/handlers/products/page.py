from aiogram import types
from aiogram.fsm.context import FSMContext

from conf.config import settings
from src.buttons.products.config import GetProductCallback
from src.buttons.products.getter import get_products_buttons
from src.handlers.products.router import products_router
from src.logger import logger
from src.requests.products.products import get_products, get_product_info
from src.template.render import render


@products_router.callback_query(GetProductCallback.filter())
async def product_callback_handler(callback: types.CallbackQuery, callback_data: GetProductCallback,
                                   state: FSMContext) -> None:
    product_id = int(callback_data.id)
    try:
        await callback.message.delete()
        product = await get_product_info(product_id)
        if not product:
            await callback.message.answer(settings.NOTHING_ERROR_MSG)
        prod_photo = settings.DEFAULT_PRODUCT_PHOTO
        if product['picture_url']:
            prod_photo = product['picture_url']
        await callback.message.answer_photo(
            photo=prod_photo,
            caption=render(
                'products/prod_msg.jinja2',
                name=product['name'],
                description=product['description'],
                price=product['price'],
            ),
            parse_mode='HTML',
            reply_markup=get_products_buttons(products, cat_id)
        )
    except Exception as err:
        await callback.message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при получении товара: {err}')
