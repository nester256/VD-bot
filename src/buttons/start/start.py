from aiogram import types


login_button = types.KeyboardButton(text='Войти')


async def start_keyboard() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(
        keyboard=[[login_button], ],
        resize_keyboard=True
    )
    return markup
