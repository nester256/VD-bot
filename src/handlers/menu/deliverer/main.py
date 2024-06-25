from aiogram import types
from src.buttons.menu.deliverer.getter import get_deliverer_menu_buttons
from src.template.render import render

from conf.config import settings


async def send_menu_message_deliverer(message: types.Message) -> None:
    await message.answer_photo(
        photo=settings.MENU_PHOTO,
        caption=render(
            'menu/deliverer/menu.jinja2',
        ),
        parse_mode='HTML',
        reply_markup=get_deliverer_menu_buttons(),
    )
    return
