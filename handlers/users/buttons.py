from aiogram import types
from aiogram.types import ChatActions, InputMediaPhoto
from loader import dp
from datetime import datetime, timedelta
import asyncio
import os
import io
from utils.misc import rate_limit
import locale

# установка локали на русскую
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

filenames = [
    "png_files/Расписание%20",
    "png_files/Расписание%2",
    "png_files/Расписание%20на%20",
    "png_files/Расписание%20на%2",
    "png_files/Расписание%20на%20-1",
    "png_files/Расписание%20на%2-1"
]

suffixes = ["_page1", "_page2", "_page3", "_page4"]


@rate_limit(limit=10)
@dp.message_handler(text='Вчера')
async def btn_yesterday(message: types.Message):
    yesterday_date = datetime.now() - timedelta(1)

    date1 = yesterday_date.strftime('%d.%m.%Y')
    date2 = yesterday_date.strftime('%d.%m.%y')
    date3 = yesterday_date.strftime('%d-%m-%Y')
    date4 = yesterday_date.strftime('%d-%m-%y')

    week = yesterday_date.strftime('%A').lower()

    new_filenames = []
    for filename in filenames:
        for date in (date1, date2, date3, date4):
            for suffix in suffixes:
                new_filenames.append(f"{filename}{date}{suffix}.png")

    album = []
    found_files = False  # флаг для проверки, найден ли файл
    caption_set = False  # флаг для отслеживания, был ли уже установлен caption

    for new_filename in new_filenames:
        if os.path.exists(new_filename):
            found_files = True  # флаг для проверки, найден ли файл
            with open(new_filename, 'rb') as photo_file:
                await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
                await asyncio.sleep(0.3)
                # преобразование содержимого файла в бинарный формат
                photo_binary = io.BytesIO(photo_file.read())

                caption = (f'Расписание на <b>{yesterday_date.strftime("%d.%m")}</b> ({week})\n'
                           f'@mtkspbbot') if not caption_set else None

                media = InputMediaPhoto(media=photo_binary, caption=caption)
                album.append(media)

                caption_set = True  # флаг для отслеживания, был ли уже установлен caption

    if found_files:
        await message.answer_media_group(media=album)
    else:
        await message.answer_chat_action('typing')
        await asyncio.sleep(1)
        await message.answer("Ничего не найдено!")


@rate_limit(limit=10)
@dp.message_handler(text='Сегодня')
async def btn_today(message: types.Message):
    today_date = datetime.now()

    date1 = today_date.strftime('%d.%m.%Y')
    date2 = today_date.strftime('%d.%m.%y')
    date3 = today_date.strftime('%d-%m-%Y')
    date4 = today_date.strftime('%d-%m-%y')

    week = today_date.strftime('%A').lower()

    new_filenames = []
    for filename in filenames:
        for date in (date1, date2, date3, date4):
            for suffix in suffixes:
                new_filenames.append(f"{filename}{date}{suffix}.png")

    album = []
    found_files = False  # флаг для проверки, найден ли файл
    caption_set = False  # флаг для отслеживания, был ли уже установлен caption

    for new_filename in new_filenames:
        if os.path.exists(new_filename):
            found_files = True  # флаг для проверки, найден ли файл
            with open(new_filename, 'rb') as photo_file:
                await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
                await asyncio.sleep(0.3)
                # преобразование содержимого файла в бинарный формат
                photo_binary = io.BytesIO(photo_file.read())

                caption = (f'Расписание на <b>{today_date.strftime("%d.%m")}</b> ({week})\n'
                           f'@mtkspbbot') if not caption_set else None

                media = InputMediaPhoto(media=photo_binary, caption=caption)
                album.append(media)

                caption_set = True  # флаг для отслеживания, был ли уже установлен caption

    if found_files:
        await message.answer_media_group(media=album)
    else:
        await message.answer_chat_action('typing')
        await asyncio.sleep(1)
        await message.answer("Ничего не найдено!")


@rate_limit(limit=10)
@dp.message_handler(text='Завтра')
async def btn_tomorrow(message: types.Message):
    tomorrow_date = datetime.now() + timedelta(1)

    date1 = tomorrow_date.strftime('%d.%m.%Y')
    date2 = tomorrow_date.strftime('%d.%m.%y')
    date3 = tomorrow_date.strftime('%d-%m-%Y')
    date4 = tomorrow_date.strftime('%d-%m-%y')

    week = tomorrow_date.strftime('%A').lower()

    new_filenames = []
    for filename in filenames:
        for date in (date1, date2, date3, date4):
            for suffix in suffixes:
                new_filenames.append(f"{filename}{date}{suffix}.png")

    album = []
    found_files = False  # флаг для проверки, найден ли файл
    caption_set = False  # флаг для отслеживания, был ли уже установлен caption

    for new_filename in new_filenames:
        if os.path.exists(new_filename):
            found_files = True  # флаг для проверки, найден ли файл
            with open(new_filename, 'rb') as photo_file:
                await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
                await asyncio.sleep(0.3)
                # преобразование содержимого файла в бинарный формат
                photo_binary = io.BytesIO(photo_file.read())

                caption = (f'Расписание на <b>{tomorrow_date.strftime("%d.%m")}</b> ({week})\n'
                           f'@mtkspbbot') if not caption_set else None

                media = InputMediaPhoto(media=photo_binary, caption=caption)
                album.append(media)

                caption_set = True  # флаг для отслеживания, был ли уже установлен caption

    if found_files:
        await message.answer_media_group(media=album)
    else:
        await message.answer_chat_action('typing')
        await asyncio.sleep(1)
        await message.answer("Ничего не найдено!")
