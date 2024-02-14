from aiogram import types


async def contact_keyboard():
    send_phone_button = types.KeyboardButton(text='📱 Отправить', request_contact=True)
    markup = types.ReplyKeyboardMarkup(
        keyboard=[[send_phone_button],],
        resize_keyboard=True
    )
    return markup
