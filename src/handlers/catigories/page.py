from aiogram import F, types
from aiogram.fsm.context import FSMContext

from src.buttons.categories.config import SHOW_CAT_CALLBACK, PaginationCallback
from src.buttons.categories.getter import get_categories_buttons
from src.handlers.catigories.router import categories_router
from src.logger import logger
from src.requests.categories.categories import get_categories
from src.template.render import render

from conf.config import settings


@categories_router.callback_query(F.data == SHOW_CAT_CALLBACK)
async def categories_callback_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    try:
        await callback.message.delete()
        await state.set_state(None)
        categories = await get_categories(0)
        if not categories:
            await callback.answer(settings.NOTHING_ERROR_MSG)
        await callback.message.answer_photo(
            photo=settings.CATEGORIES_PHOTO,
            caption=render(
                'categories/cat_msg.jinja2',
            ),
            parse_mode='HTML',
            reply_markup=get_categories_buttons(categories, 0),
        )
    except Exception as err:
        await callback.message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при получении категорий: {err}')


@categories_router.callback_query(PaginationCallback.filter())
async def handle_pagination_categories(
    callback: types.CallbackQuery, callback_data: PaginationCallback, state: FSMContext
):
    offset = int(callback_data.offset)
    try:
        await callback.message.delete()
        categories = await get_categories(offset)
        if not categories:
            offset = 0
            categories = await get_categories(0)
        await callback.message.answer_photo(
            photo=settings.CATEGORIES_PHOTO,
            caption=render(
                'categories/cat_msg.jinja2',
            ),
            parse_mode='HTML',
            reply_markup=get_categories_buttons(categories, offset),
        )
    except Exception as err:
        await callback.message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при получении категорий: {err}')
