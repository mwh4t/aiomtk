from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_fb = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Отмена', callback_data='cancel')
                                    ]
                                ])