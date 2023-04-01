from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вчера'),
            KeyboardButton(text='Сегодня'),
            KeyboardButton(text='Завтра')
        ]
    ],
    resize_keyboard=True
)