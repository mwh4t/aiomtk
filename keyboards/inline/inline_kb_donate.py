from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

ikb_donate = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Донат', web_app=WebAppInfo(url=f'https://www.donationalerts.com/r/mtk_bot'))
                                    ]
                                ])