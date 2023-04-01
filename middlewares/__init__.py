from aiogram import Dispatcher
from .throttling import ThrottlingMiddleware

def setup(dp: Dispatcher):
    # установление ограничений на определенные действия, выполняемые ботом
    dp.middleware.setup(ThrottlingMiddleware())