import os  # либа функций для работы с ОС
from dotenv import load_dotenv  # функция для загрузки переменных из .env

load_dotenv()  # загрузка переменных из .env
BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

admins = [
    930712559
]

# получение и присваивание значений
ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

# URI для подключения к базе данных PostgreSQL
POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'
