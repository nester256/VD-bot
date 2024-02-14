from aiogram import types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from src.buttons.login.contact_getter import contact_keyboard
from src.handlers.login.router import login_router
from src.state.login import LoginState
from src.template.render import render


# @login_router.message(Command("login",))
@login_router.message(F.text == "Войти", LoginState.unauthorized)  # TODO узнать можно ли так
async def share_number(message: types.Message, state: FSMContext):
    await state.set_state(LoginState.get_phone)
    await message.answer("Нажмите на кнопку ниже, чтобы отправить контакт", reply_markup=await contact_keyboard())


@login_router.message(LoginState.get_phone)
async def get_phone_num(message: types.Message, state: FSMContext):
    contact = message.contact
    await message.answer(
        render("login/greeting.jinja2", contact=contact),  # Учимся юзать джиджджжду
        reply_markup=types.ReplyKeyboardRemove()
    )

    await state.set_state(LoginState.authorized_client)
    # TODO Наверное тут разграничивать кто есть кто по жизни
    # TODO Либо регистрировать либо авторизовывать на беке. Еще стейтов тогда
