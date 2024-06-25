from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_deliverer_menu_buttons() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text='Активный заказ',
            callback_data='start.sure',
        ),
        InlineKeyboardButton(
            text='История заказов',
            callback_data='start.sure',
        ),
    )
    builder.row(
        InlineKeyboardButton(
            text='Список заказов',
            callback_data='start.sure',
        )
    )
    return builder.as_markup()
