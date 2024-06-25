from aiogram import F, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from src.buttons.login.config import START_SURE_CALLBACK
from src.buttons.login.getter import get_start_button
from src.handlers.main.router import main_router
from src.handlers.menu.customer.main import send_menu_message_customer
from src.handlers.menu.deliverer.main import send_menu_message_deliverer
from src.logger import logger
from src.requests.user import create_user_request
from src.requests.user.user import get_user_info
from src.template.render import render

from conf.config import settings


@main_router.message(
    Command(
        'start',
    )
)
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    try:
        access_token = (await state.get_data()).get('access_token')
        if access_token is not None:
            info = await get_user_info()
            if info['role'] == 'deliverer':
                await send_menu_message_deliverer(message)
                return
            addr = info['address']
            if not addr:
                addr = settings.NEW_CUSTOMER_ADDR
            await send_menu_message_customer(message, addr)
            return

        user = await create_user_request(id=message.from_user.id, username=message.from_user.username)
        if not user:
            await message.answer(settings.DEFAULT_ERROR_MSG)
            return

        await message.answer(
            text=render('start/greeting.jinja2', name=message.from_user.first_name, user_id=message.from_user.id),
            parse_mode='HTML',
            reply_markup=get_start_button(),
        )
        return
    except Exception as err:
        await message.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка при /start: {err}')
        raise err


@main_router.callback_query(F.data == START_SURE_CALLBACK)
async def start_sure_handler(callback: types.CallbackQuery) -> None:
    try:
        await callback.answer('')
        await send_menu_message_customer(callback.message, settings.NEW_CUSTOMER_ADDR)
        return
    except Exception as err:
        await callback.answer(settings.DEFAULT_ERROR_MSG)
        logger.error(f'Ошибка start_sure: {err}')
        raise err
