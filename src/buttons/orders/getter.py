from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.buttons.menu.customer.config import SHOW_MENU_CALLBACK


def get_orders_button() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text='⬅️',
            callback_data=SHOW_MENU_CALLBACK,
        )
    )
    return builder.as_markup()
