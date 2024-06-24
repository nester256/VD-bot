from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from src.buttons.categories.config import ProductCallback
from src.buttons.menu.customer.config import SHOW_MENU_CALLBACK
from src.buttons.product.config import AddToBasketCallback


def get_product_buttons(product: dict) -> InlineKeyboardMarkup:
    kb = [
        [
            types.InlineKeyboardButton(
                text="⬅️",
                callback_data=ProductCallback(
                    id=product['category_id'],
                ).pack()
            ),
            types.InlineKeyboardButton(
                text="🏠",
                callback_data=SHOW_MENU_CALLBACK
            ),
            types.InlineKeyboardButton(
                text="🛒",
                callback_data=AddToBasketCallback(
                    id=int(product['id']),
                    name=str(product['name']),
                    price=float(product['price'])
                ).pack()
            )
        ],
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)
