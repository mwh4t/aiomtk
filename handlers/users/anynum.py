from aiogram import types
from aiogram.types import ChatActions, InputMediaPhoto
from loader import dp
from datetime import datetime
import os
import io
import asyncio
import locale
import random
from handlers.users.msgs import msgs1

# установка локали на русскую
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


# handler будет запущен, если сообщение содержит только цифры
@dp.message_handler(lambda message: message.text.isdigit())
async def any_number(message: types.Message):
    user_day = int(message.text)

    date = datetime.now()

    # обработчик для чисел выше, чем в текущем месяце
    try:
        selected_date = date.replace(day=user_day)
    except (ValueError, OverflowError):
        random_msg = random.choice(msgs1)
        await message.answer(random_msg)
        return

    next_month_day = 1
    next_month = date.replace(month=date.month + 1, day=next_month_day)
    if date.month == 12:
        next_month = next_month.replace(month=1, year=date.year + 1)

    filenames = [
        "png_files/Расписание%20",
        "png_files/Расписание%2",
        "png_files/Расписание%20на%20",
        "png_files/Расписание%20на%2",
        "png_files/Расписание%20на%20-1",
        "png_files/Расписание%20на%2-1",
    ]

    additions = ["", "-объединены"]

    suffixes = ["_page1", "_page2", "_page3", "_page4"]

    new_filenames = []
    new_next_month_filenames = []
    for filename in filenames:
        for addition in additions:
            for suffix in suffixes:
                # элементы списка для текущего месяца
                new_filenames.append(f"{filename}{message.text:0>2}.{date.month:0>2}.{date.year}{addition}{suffix}.png")
                new_filenames.append(
                    f"{filename}{message.text:0>2}.{date.month:0>2}.{date.year % 100}{addition}{suffix}.png")
                new_filenames.append(f"{filename}{message.text:0>2}-{date.month:0>2}-{date.year}{addition}{suffix}.png")
                new_filenames.append(
                    f"{filename}{message.text:0>2}-{date.month:0>2}-{date.year % 100}{addition}{suffix}.png")

                # элементы списка для следующего месяца
                new_next_month_filenames.append(
                    f"{filename}{message.text:0>2}.{next_month.month:0>2}.{date.year}{addition}{suffix}.png")
                new_next_month_filenames.append(
                    f"{filename}{message.text:0>2}.{next_month.month:0>2}.{date.year % 100}{addition}{suffix}.png")
                new_next_month_filenames.append(
                    f"{filename}{message.text:0>2}-{next_month.month:0>2}-{date.year}{addition}{suffix}.png")
                new_next_month_filenames.append(
                    f"{filename}{message.text:0>2}-{next_month.month:0>2}-{date.year % 100}{addition}{suffix}.png")

    album = []
    # отправка стопки для текущего месяца
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
                week = selected_date.strftime("%A").lower()

                caption = (f'Расписание на <b>{selected_date.strftime("%d.%m")}</b> ({week})\n'
                           f'@mtkspbbot') if not caption_set else None

                media = InputMediaPhoto(media=photo_binary, caption=caption)
                album.append(media)

                caption_set = True  # флаг для отслеживания, был ли уже установлен caption

    if found_files:
        await message.answer_media_group(media=album)
    else:
        album = []
        # отправка стопки для следующего месяца
        found_files1 = False  # флаг для проверки, найден ли файл
        caption_set = False  # флаг для отслеживания, был ли уже установлен caption

        for new_next_month_filename in new_next_month_filenames:
            if os.path.exists(new_next_month_filename):
                found_files1 = True  # флаг для проверки, найден ли файл
                with open(new_next_month_filename, 'rb') as photo_file:
                    await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
                    await asyncio.sleep(0.3)
                    # преобразование содержимого файла в бинарный формат
                    photo_binary = io.BytesIO(photo_file.read())
                    selected_date = date.replace(day=user_day, month=next_month.month)
                    week = selected_date.strftime("%A").lower()
                    caption = (f'Расписание на <b>{selected_date.strftime("%d.%m")}</b> ({week})\n'
                               f'@mtkspbbot') if not caption_set else None

                    media = InputMediaPhoto(media=photo_binary, caption=caption)
                    album.append(media)

                    caption_set = True  # флаг для отслеживания, был ли уже установлен caption

        if found_files1:
            await message.answer_media_group(media=album)
        else:
            await message.answer_chat_action('typing')
            await asyncio.sleep(1)
            await message.answer("Ничего не найдено!")
