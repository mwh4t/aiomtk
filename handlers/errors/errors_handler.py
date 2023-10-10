import logging

from aiogram.utils.exceptions import (Unauthorized, MessageCantBeDeleted, MessageToDeleteNotFound, MessageNotModified,
                                      MessageTextIsEmpty, CantParseEntities, CantDemoteChatCreator, InvalidQueryID,
                                      RetryAfter, TelegramAPIError, BadRequest)

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    # неавторизованный
    if isinstance(exception, Unauthorized):
        logging.info(f'Unauthorized: {exception}')
        return True

    # сообщение не может быть удалено
    if isinstance(exception, MessageCantBeDeleted):
        logging.info('Message cant be deleted.')
        return True

    # сообщение для удаления не найдено
    if isinstance(exception, MessageToDeleteNotFound):
        logging.info('Message to delete not found.')
        return True

    # сообщение не изменено
    if isinstance(exception, MessageNotModified):
        logging.info('Message is not modified.')
        return True

    # текст сообщения пуст
    if isinstance(exception, MessageTextIsEmpty):
        logging.debug('Message text is empty.')
        return True

    # не удаётся разобрать объекты
    if isinstance(exception, CantParseEntities):
        logging.debug(f'Cant parse entities. ExceptionArgs: {exception.args}')
        return True

    # невозможно понизить создателя чата
    if isinstance(exception, CantDemoteChatCreator):
        logging.debug('Cant demote chat creator.')
        return True

    # недопустимый идентификатор запроса
    if isinstance(exception, InvalidQueryID):
        logging.exception(f'InvalidQueryID: {exception} \nUpdate: {update}')
        return True

    # повторить после
    if isinstance(exception, RetryAfter):
        logging.exception(f'RetryAfter: {exception} \nUpdate: {update}')
        return True

    # неверный запрос
    if isinstance(exception, BadRequest):
        logging.exception(f'BadRequest: {exception} \nUpdate: {update}')
        return True

    # ошибка API Telegram
    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {update} \nUpdate: {update}')
        return True

    # другая причина
    logging.exception(f'Update: {update} \nException: {exception}')
