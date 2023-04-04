from aiogram import types
from loader import dp
import requests # либа для выполнения HTTP-запросов
import fitz # либа для работы с PDF
from datetime import datetime

# handler будет запущен, если сообщение содержит только цифры
@dp.message_handler(lambda message: message.text.isdigit())
async def any_number(message: types.Message):
    date = datetime.now()
    link1 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{message.text:0>2}.{date.month:0>2}.{date.year}.pdf"
    link2 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{message.text:0>2}-{date.month:0>2}-{date.year}.pdf"
    response1 = requests.get(link1) # отправка HTTP GET запроса на сайт
    response2 = requests.get(link2)  # отправка HTTP GET запроса на сайт
    if response1.status_code == 200 and response2.status_code == 200:
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
    elif response1.status_code == 200 and response2.status_code == 404:
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
    else:
        await message.answer('Ничего не найдено!')