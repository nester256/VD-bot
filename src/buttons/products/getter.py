from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from src.buttons.menu.customer.config import SHOW_MENU_CALLBACK
from src.buttons.products.config import ProductPaginationCallback, GetProductCallback


def get_products_buttons(data: list, cat_id: int, offset: int = 0) -> InlineKeyboardMarkup:
    kb = [
        [
            types.InlineKeyboardButton(
                text=f"{product['name']} - ₽{product['price']}",
                callback_data=GetProductCallback(
                    id=product['id'],
                ).pack()
            ),
        ] for product in data
    ]
    if data:
        pagination_buttons = create_prod_pagination_buttons(cat_id, offset)
        kb.append(pagination_buttons)
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def create_prod_pagination_buttons(cat_id: int, offset: int = 0):
    return [
        types.InlineKeyboardButton(
            text="⬅️",
            callback_data=ProductPaginationCallback(
                action="prev", offset=max(0, offset - 10), c_id=cat_id
            ).pack()
        ),
        types.InlineKeyboardButton(
            text="🏠",
            callback_data=SHOW_MENU_CALLBACK
        ),
        types.InlineKeyboardButton(
            text="➡️",
            callback_data=ProductPaginationCallback(
                action="next", offset=offset + 10, c_id=cat_id
            ).pack()
        )
    ]
