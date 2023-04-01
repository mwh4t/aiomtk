from aiogram import types
from loader import dp
from utils.misc import rate_limit

@rate_limit(limit=10)
@dp.message_handler(text='/tt')
async def command_tt(message: types.Message):
    await message.answer(f'<b>Понедельник-пятница</b>\n'
                         f'<i>I пара:</i> 9.30 - 11.00\n'
                         f'<i>II пара:</i> 11.10 - 12.40\n'
                         f'<i>III пара:</i> 13.20 - 14.50\n'
                         f'<i>IV пара:</i> 15.00 - 16.30\n'
                         f'<i>V пара:</i> 16.40 - 18.10\n'
                         f'<i>VI пара:</i> 18.20 - 19.50\n\n'
                         f'<b>Суббота</b>\n'
                         f'<i>I пара:</i> 9.30 - 11.00\n'
                         f'<i>II пара:</i> 11.10 - 12.40\n'
                         f'<i>III пара:</i> 13.00 - 14.30\n'
                         f'<i>IV пара:</i> 14.40 - 16.10\n'
                         f'<i>V пара:</i> 16.20 - 17.50\n'
                         f'<i>VI пара:</i> 18.00 - 19.30')