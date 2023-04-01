from aiogram import types
from loader import dp
import requests # либа для выполнения HTTP-запросов
import fitz # либа для работы с PDF
from datetime import datetime, timedelta

@dp.message_handler(text='Вчера')
async def btn_yesterday(message: types.Message):
    try:
        date = str(datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%Y'))
        link = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date}.pdf"
        response = requests.get(link) # отправка HTTP GET запроса на сайт
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        file_path = "pdf.pdf" # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify) # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png") # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    except:
        await message.answer('Ничего не найдено!')

@dp.message_handler(text='Сегодня')
async def btn_today(message: types.Message):
    try:
        date = str(datetime.strftime(datetime.now(), '%d.%m.%Y'))
        link = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date}.pdf"
        response = requests.get(link) # отправка HTTP GET запроса на сайт
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        file_path = "pdf.pdf" # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify) # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png") # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    except:
        await message.answer('Ничего не найдено!')

@dp.message_handler(text='Завтра')
async def btn_tomorrow(message: types.Message):
    try:
        date = str(datetime.strftime(datetime.now() + timedelta(1), '%d.%m.%Y'))
        link = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date}.pdf"
        response = requests.get(link) # отправка HTTP GET запроса на сайт
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        file_path = "pdf.pdf" # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify) # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png") # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    except:
        await message.answer('Ничего не найдено!')