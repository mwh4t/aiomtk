from aiogram.dispatcher.filters.state import StatesGroup, State


class fb_states(StatesGroup):
    waiting_for_fb = State()
