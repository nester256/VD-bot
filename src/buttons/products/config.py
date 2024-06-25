from aiogram.filters.callback_data import CallbackData


class ProductPaginationCallback(CallbackData, prefix='page_p'):
    c_id: int
    action: str
    offset: int


class GetProductCallback(CallbackData, prefix='get_p'):
    id: int
