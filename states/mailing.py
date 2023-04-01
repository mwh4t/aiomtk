from aiogram.dispatcher.filters.state import StatesGroup, State

class bot_mailing(StatesGroup):
    text = State()
    state = State()
    photo = State()