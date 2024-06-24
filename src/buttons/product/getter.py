from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from src.buttons.categories.config import ProductCallback
from src.buttons.login.config import START_SURE_CALLBACK
from src.buttons.menu.customer.config import SHOW_MENU_CALLBACK


def get_product_buttons(product: dict) -> InlineKeyboardMarkup:
    kb = [
        [
            types.InlineKeyboardButton(
                text="Назад",
                callback_data=ProductCallback(
                    id=product['category_id'],
                ).pack()
            ),
            types.InlineKeyboardButton(
                text="🏠",
                callback_data=SHOW_MENU_CALLBACK
            ),
            types.InlineKeyboardButton(
                text="В корзину",
                # TODO сделать колбек на добавление в корзину
                callback_data=START_SURE_CALLBACK
            )
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)

