from aiogram.fsm.state import State, StatesGroup


class LoginState(StatesGroup):
    unauthorized = State()

    get_phone = State()

    authorized_client = State()

    authorized_courier = State()
