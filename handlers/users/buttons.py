from aiogram import types
from aiogram.types import ChatActions
from loader import dp
import requests # либа для выполнения HTTP-запросов
import fitz # либа для работы с PDF
from datetime import datetime, timedelta

@dp.message_handler(text='Вчера')
async def btn_yesterday(message: types.Message):
    await message.answer_chat_action('typing')
    date1 = str(datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%Y'))
    date2 = str(datetime.strftime(datetime.now() - timedelta(1), '%d-%m-%Y'))
    date3 = str(datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%Y'))
    date4 = str(datetime.strftime(datetime.now() - timedelta(1), '%d-%m-%Y'))
    link1 = f"https://mtkspb.ru/public/educational/Расписание%20{date1}.pdf"
    link2 = f"https://mtkspb.ru/public/educational/Расписание%20{date2}.pdf"
    link3 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date3}.pdf"
    link4 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date4}.pdf"
    response1 = requests.get(link1) # отправка HTTP GET запроса на сайт
    response2 = requests.get(link2) # отправка HTTP GET запроса на сайт
    response3 = requests.get(link3) # отправка HTTP GET запроса на сайт
    response4 = requests.get(link4) # отправка HTTP GET запроса на сайт
    if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 404 and response4.status_code == 404:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response2.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    elif response1.status_code == 200 and response2.status_code == 404 and response3.status_code == 404 and response4.status_code == 404:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response1.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    elif response1.status_code == 404 and response2.status_code == 404 and response3.status_code == 200 and response4.status_code == 200:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response4.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    elif response1.status_code == 404 and response2.status_code == 404 and response3.status_code == 200 and response4.status_code == 404:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response3.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    else:
        await message.answer_chat_action('typing')
        await message.answer('Ничего не найдено!')

@dp.message_handler(text='Сегодня')
async def btn_today(message: types.Message):
    await message.answer_chat_action('typing')
    date1 = str(datetime.strftime(datetime.now(), '%d.%m.%Y'))
    date2 = str(datetime.strftime(datetime.now(), '%d-%m-%Y'))
    date3 = str(datetime.strftime(datetime.now(), '%d.%m.%Y'))
    date4 = str(datetime.strftime(datetime.now(), '%d-%m-%Y'))
    link1 = f"https://mtkspb.ru/public/educational/Расписание%20{date1}.pdf"
    link2 = f"https://mtkspb.ru/public/educational/Расписание%20{date2}.pdf"
    link3 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date3}.pdf"
    link4 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date4}.pdf"
    response1 = requests.get(link1) # отправка HTTP GET запроса на сайт
    response2 = requests.get(link2) # отправка HTTP GET запроса на сайт
    response3 = requests.get(link3) # отправка HTTP GET запроса на сайт
    response4 = requests.get(link4) # отправка HTTP GET запроса на сайт
    if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 404 and response4.status_code == 404:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response2.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    elif response1.status_code == 200 and response2.status_code == 404 and response3.status_code == 404 and response4.status_code == 404:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response1.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    elif response1.status_code == 404 and response2.status_code == 404 and response3.status_code == 200 and response4.status_code == 200:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response4.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    elif response1.status_code == 404 and response2.status_code == 404 and response3.status_code == 200 and response4.status_code == 404:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response3.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    else:
        await message.answer_chat_action('typing')
        await message.answer('Ничего не найдено!')

@dp.message_handler(text='Завтра')
async def btn_tomorrow(message: types.Message):
    await message.answer_chat_action('typing')
    date1 = str(datetime.strftime(datetime.now() + timedelta(1), '%d.%m.%Y'))
    date2 = str(datetime.strftime(datetime.now() + timedelta(1), '%d-%m-%Y'))
    date3 = str(datetime.strftime(datetime.now() + timedelta(1), '%d.%m.%Y'))
    date4 = str(datetime.strftime(datetime.now() + timedelta(1), '%d-%m-%Y'))
    link1 = f"https://mtkspb.ru/public/educational/Расписание%20{date1}.pdf"
    link2 = f"https://mtkspb.ru/public/educational/Расписание%20{date2}.pdf"
    link3 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date3}.pdf"
    link4 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date4}.pdf"
    response1 = requests.get(link1) # отправка HTTP GET запроса на сайт
    response2 = requests.get(link2) # отправка HTTP GET запроса на сайт
    response3 = requests.get(link3) # отправка HTTP GET запроса на сайт
    response4 = requests.get(link4) # отправка HTTP GET запроса на сайт
    if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 404 and response4.status_code == 404:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response2.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    elif response1.status_code == 200 and response2.status_code == 404 and response3.status_code == 404 and response4.status_code == 404:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response1.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    elif response1.status_code == 404 and response2.status_code == 404 and response3.status_code == 200 and response4.status_code == 200:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response4.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    elif response1.status_code == 404 and response2.status_code == 404 and response3.status_code == 200 and response4.status_code == 404:
        await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
        # полученные данные сохраняются в PDF
        pdf = open("pdf.pdf", 'wb')
        pdf.write(response3.content)
        pdf.close()
        file_path = "pdf.pdf"  # путь к PDF файлу
        # дефолтные настройки
        dpi = 300
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        page = fitz.open(file_path)
        pix = page[0].get_pixmap(matrix=magnify)  # 1-ая страница PDF преобразуется в пиксельную карту
        pix.save("page.png")  # пиксельная карта сохраняется в формате .png
        img = open("page.png", 'rb')
        await message.answer_photo(photo=img, caption='@mtkspbbot')
    else:
        await message.answer_chat_action('typing')
        await message.answer('Ничего не найдено!')