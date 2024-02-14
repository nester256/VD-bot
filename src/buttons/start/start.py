from aiogram import types


async def start_keyboard() -> types.ReplyKeyboardMarkup:
    start_button = types.KeyboardButton(text='Войти')
    markup = types.ReplyKeyboardMarkup(
        keyboard=[[start_button],],
        resize_keyboard=True
    )
    return markup
