from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.buttons.categories.config import SHOW_CAT_CALLBACK
from src.buttons.login.config import START_SURE_CALLBACK


def get_customer_menu_buttons() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text='Категории',
            callback_data=SHOW_CAT_CALLBACK,
            # callback_data=SHOW_USER_TOP_CALLBACK,
        ),
        InlineKeyboardButton(
            text='Заказы',
            callback_data=START_SURE_CALLBACK,
        )
    )
    builder.row(
        InlineKeyboardButton(
            text='Корзина',
            callback_data=START_SURE_CALLBACK,
            # callback_data=SearchSettingsCallback(
            #     action=SearchSettingsAction.show,
            # ).pack(),
        ),
        InlineKeyboardButton(
            text='Настройки',
            callback_data=START_SURE_CALLBACK,
        ),
    )
    return builder.as_markup()