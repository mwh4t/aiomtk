from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запуск бота'),
        types.BotCommand('tt', 'Расписание звонков'),
        types.BotCommand('binfo', 'Справочная информация'),
        types.BotCommand('fb', 'Обратная связь'),
        types.BotCommand('donate', 'Помощь автору')
    ])
