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
    next_month_day = 1
    next_month = date.replace(month=date.month + 1, day=next_month_day)
    if date.month == 12:
        next_month = next_month.replace(month=1, year=date.year + 1)

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
        f"png_files/Расписание%20на%2{message.text:0>2}-{date.month:0>2}-{date.year % 100}.png",
        f"png_files/Расписание%20на%20{message.text:0>2}.{date.month:0>2}.{date.year}-1.png",
        f"png_files/Расписание%20на%20{message.text:0>2}.{date.month:0>2}.{date.year % 100}-1.png",
        f"png_files/Расписание%20на%2{message.text:0>2}.{date.month:0>2}.{date.year % 100}-1.png",
        f"png_files/Расписание%20на%20{message.text:0>2}-{date.month:0>2}-{date.year}-1.png",
        f"png_files/Расписание%20на%20{message.text:0>2}-{date.month:0>2}-{date.year % 100}-1.png",
        f"png_files/Расписание%20на%2{message.text:0>2}-{date.month:0>2}-{date.year % 100}-1.png"
    ]

    next_month_filenames = [
        f"png_files/Расписание%20{message.text:0>2}.{next_month.month:0>2}.{date.year}.png",
        f"png_files/Расписание%20{message.text:0>2}.{next_month.month:0>2}.{date.year % 100}.png",
        f"png_files/Расписание%2{message.text:0>2}.{next_month.month:0>2}.{date.year % 100}.png",
        f"png_files/Расписание%20{message.text:0>2}-{next_month.month:0>2}-{date.year}.png",
        f"png_files/Расписание%20{message.text:0>2}-{next_month.month:0>2}-{date.year % 100}.png",
        f"png_files/Расписание%2{message.text:0>2}-{next_month.month:0>2}-{date.year % 100}.png",
        f"png_files/Расписание%20на%20{message.text:0>2}.{next_month.month:0>2}.{date.year}.png",
        f"png_files/Расписание%20на%20{message.text:0>2}.{next_month.month:0>2}.{date.year % 100}.png",
        f"png_files/Расписание%20на%2{message.text:0>2}.{next_month.month:0>2}.{date.year % 100}.png",
        f"png_files/Расписание%20на%20{message.text:0>2}-{next_month.month:0>2}-{date.year}.png",
        f"png_files/Расписание%20на%20{message.text:0>2}-{next_month.month:0>2}-{date.year % 100}.png",
        f"png_files/Расписание%20на%2{message.text:0>2}-{next_month.month:0>2}-{date.year % 100}.png",
        f"png_files/Расписание%20на%20{message.text:0>2}.{next_month.month:0>2}.{date.year}-1.png",
        f"png_files/Расписание%20на%20{message.text:0>2}.{next_month.month:0>2}.{date.year % 100}-1.png",
        f"png_files/Расписание%20на%2{message.text:0>2}.{next_month.month:0>2}.{date.year % 100}-1.png",
        f"png_files/Расписание%20на%20{message.text:0>2}-{next_month.month:0>2}-{date.year}-1.png",
        f"png_files/Расписание%20на%20{message.text:0>2}-{next_month.month:0>2}-{date.year % 100}-1.png",
        f"png_files/Расписание%20на%2{message.text:0>2}-{next_month.month:0>2}-{date.year % 100}-1.png"
    ]

    filenames.extend(next_month_filenames)

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
