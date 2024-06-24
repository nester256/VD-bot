from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_deliverer_menu_buttons() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text='Активный заказ',
            callback_data='start.sure',
            # callback_data=SHOW_USER_TOP_CALLBACK,
        ),
        InlineKeyboardButton(
            text='История заказов',
            callback_data='start.sure',
            # callback_data=SHOW_FORM_CALLBACK,
        )
    )
    builder.row(
        InlineKeyboardButton(
            text='Список заказов',
            callback_data='start.sure',
            # callback_data=SEARCH_FORM_CALLBACK,
        )
    )
    return builder.as_markup()