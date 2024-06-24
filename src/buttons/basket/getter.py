from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from src.buttons.categories.config import ProductCallback
from src.buttons.product.config import RemoveBasketCallback, CREATE_ORDER_CALLBACK


def get_basket_buttons(cart: list) -> InlineKeyboardMarkup:
    kb = [
        [
            types.InlineKeyboardButton(
                text=f" {product['name']} - ₽{product['price']} ",
                callback_data=ProductCallback(
                    id=product['id'],
                ).pack()
            ),
            types.InlineKeyboardButton(
                text=f"🗑️",
                callback_data=RemoveBasketCallback(
                    id=product['id'],
                ).pack()
            ),
        ] for product in cart
    ]
    default_kb = [
        types.InlineKeyboardButton(
            text=f" Заказать ✅ ",
            callback_data=CREATE_ORDER_CALLBACK
        ),
    ]
    kb.append(default_kb)
    return types.InlineKeyboardMarkup(inline_keyboard=kb)
