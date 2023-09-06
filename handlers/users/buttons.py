from aiogram import types
from aiogram.types import ChatActions
from loader import dp
import requests # либа для выполнения HTTP-запросов
import fitz # либа для работы с PDF
from datetime import datetime, timedelta

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

@dp.message_handler(text='Вчера')
async def btn_yesterday(message: types.Message):
    await message.answer_chat_action('typing')
    date1 = str(datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%Y'))
    date2 = date3 = str(datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%y'))
    date4 = str(datetime.strftime(datetime.now() - timedelta(1), '%d-%m-%Y'))
    date5 = date6 = str(datetime.strftime(datetime.now() - timedelta(1), '%d-%m-%y'))
    link1 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date1}.pdf"
    link2 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date2}.pdf"
    link3 = f"https://mtkspb.ru/public/educational/schedule/Расписание%2{date3}.pdf"
    link4 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date4}.pdf"
    link5 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date5}.pdf"
    link6 = f"https://mtkspb.ru/public/educational/schedule/Расписание%2{date6}.pdf"
    # отправка запросов на сайт
    response1 = requests.get(link1)
    response2 = requests.get(link2)
    response3 = requests.get(link3)
    response4 = requests.get(link4)
    response5 = requests.get(link5)
    response6 = requests.get(link6)
    if (response1.status_code == 200 and response2.status_code == 404 and
            response3.status_code == 404 and response4.status_code == 404 and
            response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response1)
    # временно
    elif (response1.status_code == 200 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 200):
        await handle_pdf(message, response1)
    elif (response1.status_code == 404 and response2.status_code == 200 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response2)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 200 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response3)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 200 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response4)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 200 and response6.status_code == 404):
        await handle_pdf(message, response5)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 200):
        await handle_pdf(message, response6)
    else:
        await message.answer_chat_action('typing')
        await message.answer('Ничего не найдено!')

@dp.message_handler(text='Сегодня')
async def btn_today(message: types.Message):
    await message.answer_chat_action('typing')
    date1 = str(datetime.strftime(datetime.now(), '%d.%m.%Y'))
    date2 = date3 = str(datetime.strftime(datetime.now(), '%d.%m.%y'))
    date4 = str(datetime.strftime(datetime.now(), '%d-%m-%Y'))
    date5 = date6 = str(datetime.strftime(datetime.now(), '%d-%m-%y'))
    link1 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date1}.pdf"
    link2 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date2}.pdf"
    link3 = f"https://mtkspb.ru/public/educational/schedule/Расписание%2{date3}.pdf"
    link4 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date4}.pdf"
    link5 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date5}.pdf"
    link6 = f"https://mtkspb.ru/public/educational/schedule/Расписание%2{date6}.pdf"
    # отправка запросов на сайт
    response1 = requests.get(link1)
    response2 = requests.get(link2)
    response3 = requests.get(link3)
    response4 = requests.get(link4)
    response5 = requests.get(link5)
    response6 = requests.get(link6)
    if (response1.status_code == 200 and response2.status_code == 404 and
            response3.status_code == 404 and response4.status_code == 404 and
            response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response1)
    # временно
    elif (response1.status_code == 200 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 200):
        await handle_pdf(message, response1)
    elif (response1.status_code == 404 and response2.status_code == 200 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response2)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 200 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response3)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 200 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response4)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 200 and response6.status_code == 404):
        await handle_pdf(message, response5)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 200):
        await handle_pdf(message, response6)
    else:
        await message.answer_chat_action('typing')
        await message.answer('Ничего не найдено!')

@dp.message_handler(text='Завтра')
async def btn_tomorrow(message: types.Message):
    await message.answer_chat_action('typing')
    date1 = str(datetime.strftime(datetime.now() + timedelta(1), '%d.%m.%Y'))
    date2 = date3 = str(datetime.strftime(datetime.now() + timedelta(1), '%d.%m.%y'))
    date4 = str(datetime.strftime(datetime.now() + timedelta(1), '%d-%m-%Y'))
    date5 = date6 = str(datetime.strftime(datetime.now() + timedelta(1), '%d-%m-%y'))
    link1 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date1}.pdf"
    link2 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date2}.pdf"
    link3 = f"https://mtkspb.ru/public/educational/schedule/Расписание%2{date3}.pdf"
    link4 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date4}.pdf"
    link5 = f"https://mtkspb.ru/public/educational/schedule/Расписание%20{date5}.pdf"
    link6 = f"https://mtkspb.ru/public/educational/schedule/Расписание%2{date6}.pdf"
# отправка запросов на сайт
    response1 = requests.get(link1)
    response2 = requests.get(link2)
    response3 = requests.get(link3)
    response4 = requests.get(link4)
    response5 = requests.get(link5)
    response6 = requests.get(link6)
    if (response1.status_code == 200 and response2.status_code == 404 and
            response3.status_code == 404 and response4.status_code == 404 and
            response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response1)
    # временно
    elif (response1.status_code == 200 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 200):
        await handle_pdf(message, response1)
    elif (response1.status_code == 404 and response2.status_code == 200 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response2)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 200 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response3)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 200 and
          response5.status_code == 404 and response6.status_code == 404):
        await handle_pdf(message, response4)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 200 and response6.status_code == 404):
        await handle_pdf(message, response5)
    elif (response1.status_code == 404 and response2.status_code == 404 and
          response3.status_code == 404 and response4.status_code == 404 and
          response5.status_code == 404 and response6.status_code == 200):
        await handle_pdf(message, response6)
    else:
        await message.answer_chat_action('typing')
        await message.answer('Ничего не найдено!')