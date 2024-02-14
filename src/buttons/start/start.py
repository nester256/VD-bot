from aiogram import types


login_button = 'Войти'


async def start_keyboard() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=login_button)], ],
        resize_keyboard=True
    )
    return markup
