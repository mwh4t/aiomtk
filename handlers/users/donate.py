from aiogram import types
from keyboards.inline import ikb_donate
from utils.misc import rate_limit
from loader import dp

@rate_limit(limit=10)
@dp.message_handler(text='/donate')
async def donate(message: types.Message):
    await message.answer('Нажми на кнопку ниже, чтобы поддержать автора', reply_markup=ikb_donate)