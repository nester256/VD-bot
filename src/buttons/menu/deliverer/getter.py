from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.buttons.menu.deliverer.config import SHOW_ACTIVE_ORDERS, SHOW_AWAITING_ORDERS, SHOW_DELIVERY_MENU


def get_deliverer_menu_buttons() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text='Активный заказ',
            callback_data=SHOW_ACTIVE_ORDERS,
        ),
        InlineKeyboardButton(
            text='История заказов',
            callback_data=SHOW_DELIVERY_MENU,
        ),
    )
    builder.row(
        InlineKeyboardButton(
            text='Список заказов',
            callback_data=SHOW_AWAITING_ORDERS,
        )
    )
    return builder.as_markup()
