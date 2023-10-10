from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states import fb_states
import logging  # предоставляет способ записи сообщений в файл или консоль
from keyboards.inline import ikb_fb
from data.config import admins
import random
from handlers.users.msgs import msgs
from utils.misc import rate_limit


@rate_limit(limit=10)
@dp.message_handler(Command('fb'))
async def fb(message: types.Message):
    await message.answer('Напишите, что хотите отправить автору', reply_markup=ikb_fb)
    await fb_states.waiting_for_fb.set()  # устанавливает состояние диалога в waiting_for_fb


@dp.callback_query_handler(text='cancel', state=fb_states.waiting_for_fb)
async def cancel_feedback(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    await state.finish()  # сбрасывает состояние диалога


@dp.message_handler(state=fb_states.waiting_for_fb)
async def state1(message: types.Message, state: FSMContext):
    user = message.from_user.username
    user_id = message.from_user.id
    answer = message.text
    await state.finish()  # сбрасывает состояние диалога
    await message.answer('Отзыв отправлен!')
    for admin in admins:
        try:
            await dp.bot.send_message(chat_id=admin,
                                      text=f'<b>Поступил отзыв от @{user}</b> (ID: "{user_id}"):\n'
                                           f'"{answer}"')
        except Exception as err:
            logging.exception(err)


@dp.message_handler()
async def answer(message: types.Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.text.split('"')[1]
        for admin in admins:
            try:
                await dp.bot.send_message(chat_id=admin, text='Ответ отправлен!')
            except Exception as err:
                logging.exception(err)
        await dp.bot.send_message(chat_id=user_id, text=f'<b>Поступил ответ на отзыв</b>:\n'
                                                        f'"{message.text}"')
    else:
        random_msg = random.choice(msgs)
        await message.answer(random_msg)
