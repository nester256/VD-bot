from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from src.buttons.menu.deliverer.config import SHOW_DELIVERY_MENU
from src.buttons.orders.deliverer.config import SetDeliverer, SetDone


def get_orders_deliverer_button(orders: list) -> InlineKeyboardMarkup:
    kb = [
        [
            types.InlineKeyboardButton(
                text=f"Принять заказ: {order['order_id']}",
                callback_data=SetDeliverer(
                    order_id=order['order_id'],
                ).pack(),
            ),
        ]
        for order in orders
    ]
    kb.append(
        [
            types.InlineKeyboardButton(text='🏠', callback_data=SHOW_DELIVERY_MENU),
        ]
    )
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def get_active_deliverer_button(orders: list) -> InlineKeyboardMarkup:
    kb = [
        [
            types.InlineKeyboardButton(
                text=f"Заказ доставлен: {order['order_id']}",
                callback_data=SetDone(
                    order_id=order['order_id'],
                ).pack(),
            ),
        ]
        for order in orders
    ]
    kb.append(
        [
            types.InlineKeyboardButton(text='🏠', callback_data=SHOW_DELIVERY_MENU),
        ]
    )
    return types.InlineKeyboardMarkup(inline_keyboard=kb)
