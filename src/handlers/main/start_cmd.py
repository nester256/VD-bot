from aiogram import types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from src.buttons.start.start import start_keyboard
from src.handlers.main.router import main_router
from src.state.login import LoginState


@main_router.message(Command("start",))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(LoginState.unauthorized)
    await message.answer("Спасибо что пришли", reply_markup=await start_keyboard())
