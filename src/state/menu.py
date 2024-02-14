from aiogram.fsm.state import StatesGroup, State


class MenuClientState(StatesGroup):
    restaurants_list = State()

    enter_code = State()

    authorized = State()
