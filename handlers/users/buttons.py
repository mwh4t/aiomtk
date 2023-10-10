from aiogram import types
from aiogram.types import ChatActions
from loader import dp
from datetime import datetime, timedelta
import asyncio
import os
from utils.misc import rate_limit
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


@rate_limit(limit=10)
@dp.message_handler(text='Вчера')
async def btn_yesterday(message: types.Message):
    yesterday_date = datetime.now() - timedelta(1)

    date1 = yesterday_date.strftime('%d.%m.%Y')
    date2 = date3 = yesterday_date.strftime('%d.%m.%y')
    date4 = yesterday_date.strftime('%d-%m-%Y')
    date5 = date6 = yesterday_date.strftime('%d-%m-%y')

    week = yesterday_date.strftime('%A').lower()

    filenames = [
        f"png_files/Расписание%20{date1}.png",
        f"png_files/Расписание%20{date2}.png",
        f"png_files/Расписание%2{date3}.png",
        f"png_files/Расписание%20{date4}.png",
        f"png_files/Расписание%20{date5}.png",
        f"png_files/Расписание%2{date6}.png",
        f"png_files/Расписание%20на%20{date1}.png",
        f"png_files/Расписание%20на%20{date2}.png",
        f"png_files/Расписание%20на%2{date3}.png",
        f"png_files/Расписание%20на%20{date4}.png",
        f"png_files/Расписание%20на%20{date5}.png",
        f"png_files/Расписание%20на%2{date6}.png",
        f"png_files/Расписание%20на%20{date1}-1.png",
        f"png_files/Расписание%20на%20{date2}-1.png",
        f"png_files/Расписание%20на%2{date3}-1.png",
        f"png_files/Расписание%20на%20{date4}-1.png",
        f"png_files/Расписание%20на%20{date5}-1.png",
        f"png_files/Расписание%20на%2{date6}-1.png"
    ]

    for filename in filenames:
        if os.path.exists(filename):
            with open(filename, 'rb') as img:
                await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
                await asyncio.sleep(1)
                await message.answer_photo(photo=img,
                                           caption=f'Расписание на <b>{yesterday_date.strftime("%d.%m")}</b> ({week})\n'
                                                   f'@mtkspbbot')
            break
    else:
        await message.answer_chat_action('typing')
        await asyncio.sleep(1)
        await message.answer("Ничего не найдено!")


@rate_limit(limit=10)
@dp.message_handler(text='Сегодня')
async def btn_today(message: types.Message):
    today_date = datetime.now()

    date1 = today_date.strftime('%d.%m.%Y')
    date2 = date3 = today_date.strftime('%d.%m.%y')
    date4 = today_date.strftime('%d-%m-%Y')
    date5 = date6 = today_date.strftime('%d-%m-%y')

    week = today_date.strftime('%A').lower()

    filenames = [
        f"png_files/Расписание%20{date1}.png",
        f"png_files/Расписание%20{date2}.png",
        f"png_files/Расписание%2{date3}.png",
        f"png_files/Расписание%20{date4}.png",
        f"png_files/Расписание%20{date5}.png",
        f"png_files/Расписание%2{date6}.png",
        f"png_files/Расписание%20на%20{date1}.png",
        f"png_files/Расписание%20на%20{date2}.png",
        f"png_files/Расписание%20на%2{date3}.png",
        f"png_files/Расписание%20на%20{date4}.png",
        f"png_files/Расписание%20на%20{date5}.png",
        f"png_files/Расписание%20на%2{date6}.png",
        f"png_files/Расписание%20на%20{date1}-1.png",
        f"png_files/Расписание%20на%20{date2}-1.png",
        f"png_files/Расписание%20на%2{date3}-1.png",
        f"png_files/Расписание%20на%20{date4}-1.png",
        f"png_files/Расписание%20на%20{date5}-1.png",
        f"png_files/Расписание%20на%2{date6}-1.png"
    ]

    for filename in filenames:
        if os.path.exists(filename):
            with open(filename, 'rb') as img:
                await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
                await asyncio.sleep(1)
                await message.answer_photo(photo=img,
                                           caption=f'Расписание на <b>{today_date.strftime("%d.%m")}</b> ({week})\n'
                                                   f'@mtkspbbot')
            break
    else:
        await message.answer_chat_action('typing')
        await asyncio.sleep(1)
        await message.answer("Ничего не найдено!")


@rate_limit(limit=10)
@dp.message_handler(text='Завтра')
async def btn_tomorrow(message: types.Message):
    tomorrow_date = datetime.now() + timedelta(1)

    date1 = tomorrow_date.strftime('%d.%m.%Y')
    date2 = date3 = tomorrow_date.strftime('%d.%m.%y')
    date4 = tomorrow_date.strftime('%d-%m-%Y')
    date5 = date6 = tomorrow_date.strftime('%d-%m-%y')

    week = tomorrow_date.strftime('%A').lower()

    filenames = [
        f"png_files/Расписание%20{date1}.png",
        f"png_files/Расписание%20{date2}.png",
        f"png_files/Расписание%2{date3}.png",
        f"png_files/Расписание%20{date4}.png",
        f"png_files/Расписание%20{date5}.png",
        f"png_files/Расписание%2{date6}.png",
        f"png_files/Расписание%20на%20{date1}.png",
        f"png_files/Расписание%20на%20{date2}.png",
        f"png_files/Расписание%20на%2{date3}.png",
        f"png_files/Расписание%20на%20{date4}.png",
        f"png_files/Расписание%20на%20{date5}.png",
        f"png_files/Расписание%20на%2{date6}.png",
        f"png_files/Расписание%20на%20{date1}-1.png",
        f"png_files/Расписание%20на%20{date2}-1.png",
        f"png_files/Расписание%20на%2{date3}-1.png",
        f"png_files/Расписание%20на%20{date4}-1.png",
        f"png_files/Расписание%20на%20{date5}-1.png",
        f"png_files/Расписание%20на%2{date6}-1.png"
    ]

    for filename in filenames:
        if os.path.exists(filename):
            with open(filename, 'rb') as img:
                await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
                await asyncio.sleep(1)
                await message.answer_photo(photo=img,
                                           caption=f'Расписание на <b>{tomorrow_date.strftime("%d.%m")}</b> ({week})\n'
                                                   f'@mtkspbbot')
            break
    else:
        await message.answer_chat_action('typing')
        await asyncio.sleep(1)
        await message.answer("Ничего не найдено!")
