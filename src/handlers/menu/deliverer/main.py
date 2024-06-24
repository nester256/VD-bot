from aiogram import F, types
from aiogram.fsm.context import FSMContext

from conf.config import settings
from src.buttons.menu.deliverer.getter import get_deliverer_menu_buttons
from src.template.render import render


async def send_menu_message_deliverer(
        message: types.Message,
        state: FSMContext,
) -> None:
    await state.set_state(None)

    await message.answer_photo(
        photo=settings.MENU_PHOTO,
        caption=render(
            'menu/deliverer/menu.jinja2',
        ),
        parse_mode='HTML',
        reply_markup=get_deliverer_menu_buttons()
    )
    return
