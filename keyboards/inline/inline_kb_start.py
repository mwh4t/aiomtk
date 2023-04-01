from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_start = InlineKeyboardMarkup(row_width=3,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Офиц. сайт', url='https://mtkspb.ru/'),
                                        InlineKeyboardButton(text='МТК в ВК', url='https://vk.com/mtkspb'),
                                        InlineKeyboardButton(text='Инфо', callback_data='Инфо')
                                    ]
                                ])