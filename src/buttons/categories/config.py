from aiogram.filters.callback_data import CallbackData

SHOW_CAT_CALLBACK = 'categories'


class PaginationCallback(CallbackData, prefix='page'):
    action: str
    offset: int


class ProductCallback(CallbackData, prefix='product'):
    id: int
