from aiogram import types
from aiogram.types import ChatActions
from loader import dp
from datetime import datetime
import os
import asyncio


# handler будет запущен, если сообщение содержит только цифры
@dp.message_handler(lambda message: message.text.isdigit())
async def any_number(message: types.Message):
    date = datetime.now()
    filenames = [
        f"png_files/Расписание%20{message.text:0>2}.{date.month:0>2}.{date.year}.png",
        f"png_files/Расписание%20{message.text:0>2}.{date.month:0>2}.{date.year % 100}.png",
        f"png_files/Расписание%2{message.text:0>2}.{date.month:0>2}.{date.year % 100}.png",
        f"png_files/Расписание%20{message.text:0>2}-{date.month:0>2}-{date.year}.png",
        f"png_files/Расписание%20{message.text:0>2}-{date.month:0>2}-{date.year % 100}.png",
        f"png_files/Расписание%2{message.text:0>2}-{date.month:0>2}-{date.year % 100}.png",
        f"png_files/Расписание%20на%20{message.text:0>2}.{date.month:0>2}.{date.year}.png",
        f"png_files/Расписание%20на%20{message.text:0>2}.{date.month:0>2}.{date.year % 100}.png",
        f"png_files/Расписание%20на%2{message.text:0>2}.{date.month:0>2}.{date.year % 100}.png",
        f"png_files/Расписание%20на%20{message.text:0>2}-{date.month:0>2}-{date.year}.png",
        f"png_files/Расписание%20на%20{message.text:0>2}-{date.month:0>2}-{date.year % 100}.png",
        f"png_files/Расписание%20на%2{message.text:0>2}-{date.month:0>2}-{date.year % 100}.png"
    ]

    for filename in filenames:
        if os.path.exists(filename):
            with open(filename, 'rb') as img:
                await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
                await asyncio.sleep(1)
                await message.answer_photo(photo=img, caption='@mtkspbbot')
            break
    else:
        await message.answer_chat_action('typing')
        await asyncio.sleep(1)
        await message.answer("Ничего не найдено!")
