from aiogram import types
from aiogram.types import ChatActions
from loader import dp
import requests # либа для выполнения HTTP-запросов
import fitz # либа для работы с PDF
from datetime import datetime

async def handle_pdf(message: types.Message, response: requests.Response):
    await message.answer_chat_action(ChatActions.UPLOAD_PHOTO)
    # полученные данные сохраняются в PDF
    pdf = open("pdf.pdf", 'wb')
    pdf.write(response.content)
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

# handler будет запущен, если сообщение содержит только цифры
@dp.message_handler(lambda message: message.text.isdigit())
async def any_number(message: types.Message):
    await message.answer_chat_action('typing')
    date = datetime.now()
    link1 = f"https://mtkspb.ru/public/educational/Расписание%20{message.text:0>2}.{date.month:0>2}.{date.year}.pdf"
    link2 = f"https://mtkspb.ru/public/educational/Расписание%20{message.text:0>2}-{date.month:0>2}-{date.year}.pdf"
    link3 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{message.text:0>2}.{date.month:0>2}.{date.year}.pdf"
    link4 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{message.text:0>2}-{date.month:0>2}-{date.year}.pdf"
    link5 = f"https://mtkspb.ru/public/educational/Расписание%20%20{message.text:0>2}.{date.month:0>2}.{date.year}.pdf"
    link6 = f"https://mtkspb.ru/public/educational/Расписание%20%20{message.text:0>2}-{date.month:0>2}-{date.year}.pdf"
    response1 = requests.get(link1) # отправка HTTP GET запроса на сайт
    response2 = requests.get(link2) # отправка HTTP GET запроса на сайт
    response3 = requests.get(link3) # отправка HTTP GET запроса на сайт
    response4 = requests.get(link4) # отправка HTTP GET запроса на сайт
    response5 = requests.get(link5) # отправка HTTP GET запроса на сайт
    response6 = requests.get(link6) # отправка HTTP GET запроса на сайт
    if (response1.status_code == 200 and response2.status_code == 200 and
            response3.status_code == 404 and response4.status_code == 404 and
            response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response2)
    elif (response1.status_code == 200 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response1)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 200 and response4.status_code == 200 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response4)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 200 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response3)
    elif (response1.status_code == 200 and response2.status_code == 404 and
          response3.status_code == 200 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 404): # временно
        await handle_pdf(message, response1)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 200 and response6.status_code == 200):
        await handle_pdf(message, response6)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 200 and response6.status_code == 404):
        await handle_pdf(message, response5)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 200 and response4.status_code == 404 and
          response5.status_code == 200 and response6.status_code == 404): # временно
        await handle_pdf(message, response5)
    else:
        await message.answer_chat_action('typing')
        await message.answer('Ничего не найдено!')