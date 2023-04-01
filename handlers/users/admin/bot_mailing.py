from asyncio import sleep
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp
from utils.db_api import quick_commands as commands
from states import bot_mailing
from data.config import admins

@dp.message_handler(text='/mailing', chat_id=admins)
async def start_mailing(message: types.Message):
    await message.answer(f'Введите текст рассылки')
    # установление значения, используемое для отслеживания ввода рассылки
    await bot_mailing.text.set()

@dp.message_handler(state=bot_mailing.text, chat_id=admins)
async def mailing_text(message: types.Message, state: FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Добавить фото', callback_data='add_photo'),
                                          InlineKeyboardButton(text='Далее', callback_data='next'),
                                          InlineKeyboardButton(text='Отмена', callback_data='quit')
                                      ]
                                  ])
    await state.update_data(text=answer) # обновление состояния данными ответа
    await message.answer(text=answer, reply_markup=markup)
    await bot_mailing.state.set() # установление состояния

@dp.callback_query_handler(text='next', state=bot_mailing.state, chat_id=admins)
async def start(call: types.CallbackQuery, state: FSMContext):
    users = await commands.select_all_users() # извлечение пользователей из БД
    data = await state.get_data()
    text = data.get('text')
    await state.finish() # завершение состояния
    for user in users:
        try:
            await dp.bot.send_message(chat_id=user.user_id, text=text)
            await sleep(0.33) # задержка каждого сообщения
        except Exception:
            pass
    await call.message.answer('Рассылка выполнена!')

@dp.callback_query_handler(text='add_photo', state=bot_mailing.state, chat_id=admins)
async def add_photo(call: types.CallbackQuery):
    await call.message.edit_text(text='Пришлите фото')
    await bot_mailing.photo.set() # установление состояния

@dp.message_handler(state=bot_mailing.photo, content_types=types.ContentType.PHOTO, chat_id=admins)
async def mailing_text(message: types.Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id # получение самой большой фото
    await state.update_data(photo=photo_file_id) # обновление состояния
    data = await state.get_data() # извлечение текущих данных
    text = data.get('text')
    photo = data.get('photo')
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Далее', callback_data='next'),
                                          InlineKeyboardButton(text='Отмена', callback_data='quit')
                                      ]
                                  ])
    await message.answer_photo(photo=photo, caption=text, reply_markup=markup)

@dp.callback_query_handler(text='next', state=bot_mailing.photo, chat_id=admins)
async def start(call: types.CallbackQuery, state: FSMContext):
    users = await commands.select_all_users() # извлечение пользователей из БД
    data = await state.get_data() # извлечение текущих данных
    text = data.get('text')
    photo = data.get('photo')
    await state.finish() # завершение состояния
    for user in users:
        try:
            await dp.bot.send_photo(chat_id=user.user_id, photo=photo, caption=text)
            await sleep(0.33) # задержка каждого сообщения
        except Exception:
            pass
    await call.message.answer('Рассылка выполнена!')

@dp.message_handler(state=bot_mailing.text, chat_id=admins)
async def no_photo(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Отмена', callback_data='quit')
                                      ]
                                  ])
    await message.edit_text('Пришлите фото', reply_markup=markup)

@dp.callback_query_handler(text='quit', state=[bot_mailing.text, bot_mailing.photo, bot_mailing.state], chat_id=admins)
async def quit(call: types.CallbackQuery, state: FSMContext):
    await state.finish() # завершение состояния
    await call.message.answer('Рассылка отменена')