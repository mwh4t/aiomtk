import logging  # предоставляет способ записи сообщений в файл или консоль
from aiogram import types
from aiogram.types import CallbackQuery
from keyboards.default import kb_start
from keyboards.inline import ikb_start
from loader import dp
from utils.misc import rate_limit
from utils.db_api import quick_commands as commands


@rate_limit(limit=10)
@dp.message_handler(text='/start')
async def menu(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)  # выбор пользователя из БД
        if not user:
            # добавление пользователя в БД
            await commands.add_user(user_id=message.from_user.id,
                                    first_name=message.from_user.first_name,
                                    last_name=message.from_user.last_name,
                                    username=message.from_user.username)
    except Exception as ex:
        logging.exception(ex)
    await message.answer(f'Привет, {message.from_user.first_name}! Это - бот Медико-Технического колледжа 🏫🏥',
                         reply_markup=ikb_start)
    await message.answer('Подскажи, пожалуйста, какой тебя интересует день?', reply_markup=kb_start)


@dp.callback_query_handler(text='info')
async def menu(call: CallbackQuery):
    await call.answer('• Бот не является официальным\n'
                      '• Бот доступен только в ЛС\n'
                      '• Узнать расписание можно как нажав на одну из кнопок, так и отправив число месяца',
                      show_alert=True)
