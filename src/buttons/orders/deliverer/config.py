from aiogram.filters.callback_data import CallbackData


class SetDeliverer(CallbackData, prefix='set_deliverer'):
    order_id: int


class SetDone(CallbackData, prefix='set_done'):
    order_id: int
