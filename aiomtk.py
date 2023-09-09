import re
import aiohttp
import os
import fitz
import asyncio
import datetime


async def on_startup(dp):
    import middlewares
    middlewares.setup(dp)

    from loader import db
    from utils.db_api.db_gino import on_startup

    print('Подключение к PostgreSQL...')
    await on_startup(db)

    print('Создание таблиц...')
    await db.gino.create_all()
    print('Готово!')

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('Бот запущен!')


# функция для скачивания и конвертации
async def download_and_convert_pdfs(url):
    pdf_folder = 'pdf_files'
    png_folder = 'png_files'

    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    if not os.path.exists(png_folder):
        os.makedirs(png_folder)

    pattern = re.compile(r'href="(?P<link>/[^\"]+.pdf)"')

    connector = aiohttp.TCPConnector(ssl=False)  # отключение проверки SSL
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            text = await response.text()
            matches = pattern.findall(text)

            for pdf_link in matches:
                full_pdf_url = f"https://mtkspb.ru{pdf_link}"

                async with session.get(full_pdf_url) as pdf_response:
                    if pdf_response.status == 200:
                        # сохранение PDF
                        pdf_filename = os.path.join(pdf_folder, os.path.basename(pdf_link))
                        pdf_content = await pdf_response.read()
                        with open(pdf_filename, 'wb') as pdf_file:
                            pdf_file.write(pdf_content)
                        # конвертирование PDF в PNG
                        dpi = 100
                        zoom = dpi / 72
                        magnify = fitz.Matrix(zoom, zoom)
                        pdf_document = fitz.open(pdf_filename)
                        page = pdf_document[0]
                        image = page.get_pixmap(matrix=magnify)
                        image.save(os.path.join(png_folder, os.path.splitext(os.path.basename(pdf_link))[0] + '.png'),
                                   'PNG')

                        # удаление PDF
                        os.remove(pdf_filename)


# функция для выполнения каждую минуту
async def repeat_actions():
    while True:
        url_to_scrape = "https://mtkspb.ru/public/educational/schedule/index.php"
        await asyncio.sleep(3)
        print("Начало загрузки расписания...")

        # удаление старых PNG
        png_folder = 'png_files'
        for filename in os.listdir(png_folder):
            if filename.endswith(".png"):
                file_path = os.path.join(png_folder, filename)
                os.remove(file_path)

        await download_and_convert_pdfs(url_to_scrape)
        current_datetime = datetime.datetime.now()
        formatted_datetime = "(" + current_datetime.strftime("%H:%M:%S") + ")"
        print("Конец загрузки!", formatted_datetime)

        # задержка в 4 часа
        await asyncio.sleep(4 * 3600)


if __name__ == '__main__':  # проверка, выполняется ли скрипт как основная программа
    from aiogram import executor
    from handlers import dp

    loop = asyncio.get_event_loop()
    loop.create_task(repeat_actions())

    executor.start_polling(dp, on_startup=on_startup)
