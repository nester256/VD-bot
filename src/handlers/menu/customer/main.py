from aiogram import F, types
from aiogram.fsm.context import FSMContext

from conf.config import settings
from src.buttons.menu.customer.config import SHOW_MENU_CALLBACK
from src.buttons.menu.customer.getter import get_customer_menu_buttons
from src.handlers.menu.customer.router import customer_router
from src.logger import logger
from src.requests.user.user import get_user_info
from src.template.render import render


@customer_router.callback_query(F.data == SHOW_MENU_CALLBACK)
async def menu_customer_callback_handler(callback: types.CallbackQuery, state: FSMContext) -> None:
    try:
        await callback.message.delete()
        info = await get_user_info()
        addr = info['address']
        if not addr:
            addr = settings.NEW_CUSTOMER_ADDR
        await send_menu_message_customer(callback.message, state, addr)
    except Exception as err:
        await callback.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при выводе меню: {err}')

async def send_menu_message_customer(
        message: types.Message,
        state: FSMContext,
        address: str
) -> None:
    await state.set_state(None)

    await message.answer_photo(
        photo=settings.MENU_PHOTO,
        caption=render(
            'menu/customer/menu.jinja2',
            address=address
        ),
        parse_mode='HTML',
        reply_markup=get_customer_menu_buttons()
    )
    return
