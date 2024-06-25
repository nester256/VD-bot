from aiogram.filters.callback_data import CallbackData


class AddToBasketCallback(CallbackData, prefix='basket_add'):
    id: int
    name: str
    price: float


class RemoveBasketCallback(CallbackData, prefix='basket_del'):
    id: int


CREATE_ORDER_CALLBACK = 'create.order'
