from aiogram import F, types

from src.buttons.menu.deliverer.config import SHOW_DELIVERY_MENU
from src.buttons.menu.deliverer.getter import get_deliverer_menu_buttons
from src.handlers.menu.deliverer.router import delivery_router
from src.logger import logger
from src.template.render import render

from conf.config import settings


@delivery_router.callback_query(F.data == SHOW_DELIVERY_MENU)
async def menu_deliverer_callback_handler(callback: types.CallbackQuery) -> None:
    try:
        await callback.message.delete()
        await send_menu_message_deliverer(callback.message)
    except Exception as err:
        await callback.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при выводе меню доставщика: {err}')


async def send_menu_message_deliverer(message: types.Message) -> None:
    await message.answer_photo(
        photo=settings.MENU_PHOTO,
        caption=render(
            'menu/deliverer/menu.jinja2',
        ),
        parse_mode='HTML',
        reply_markup=get_deliverer_menu_buttons(),
    )
