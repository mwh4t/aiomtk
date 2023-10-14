from aiogram import types
from aiogram.types import ChatActions
from loader import dp
from datetime import datetime
import os
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

    try:
        selected_date = date.replace(day=user_day)
    except (ValueError, OverflowError):
        random_msg = random.choice(msgs1)
        await message.answer(random_msg)
        return

    week = selected_date.strftime("%A").lower()

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

    file_found = False  # флаг для проверки, был ли найден файл

    for filename in filenames:
        if os.path.exists(filename):
            with open(filename, 'rb') as img:
                await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
                await asyncio.sleep(1)

                caption = (
                    f'Расписание на <b>{selected_date.strftime("%d.%m")}</b> ({week})\n'
                    f'@mtkspbbot'
                )
                await message.answer_photo(photo=img, caption=caption, parse_mode='HTML')
                file_found = True
            break

    if not file_found:
        for filename in next_month_filenames:
            if os.path.exists(filename):
                selected_date = date.replace(day=user_day, month=next_month.month)
                week = selected_date.strftime("%A").lower()

                with open(filename, 'rb') as img:
                    await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
                    await asyncio.sleep(1)

                    caption = (
                        f'Расписание на <b>{selected_date.strftime("%d.%m")}</b> ({week})\n'
                        f'@mtkspbbot'
                    )
                    await message.answer_photo(photo=img, caption=caption, parse_mode='HTML')
                break
        else:
            await message.answer_chat_action('typing')
            await asyncio.sleep(1)
            await message.answer("Ничего не найдено!")
