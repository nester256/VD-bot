from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from src.buttons.categories.config import PaginationCallback, ProductCallback
from src.buttons.menu.customer.config import SHOW_MENU_CALLBACK


def get_categories_buttons(data: list, offset: int = 0) -> InlineKeyboardMarkup:
    kb = [
        [
            types.InlineKeyboardButton(
                text=f"{category['name']} {category['id']}",
                callback_data=ProductCallback(
                    id=category['id'],
                ).pack()
            ),
        ] for category in data
    ]
    if data:
        pagination_buttons = create_cat_pagination_buttons(offset)
        kb.append(pagination_buttons)
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def create_cat_pagination_buttons(offset=0):
    return [
        types.InlineKeyboardButton(
            text="⬅️",
            callback_data=PaginationCallback(
                action="prev", offset=max(0, offset - 5),
            ).pack()
        ),
        types.InlineKeyboardButton(
            text="🏠",
            callback_data=SHOW_MENU_CALLBACK
        ),
        types.InlineKeyboardButton(
            text="➡️",
            callback_data=PaginationCallback(
                action="next", offset=offset + 5,
            ).pack()
        )
    ]
