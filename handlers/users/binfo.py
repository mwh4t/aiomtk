from aiogram import types
from loader import dp
from utils.misc import rate_limit

@rate_limit(limit=10)
@dp.message_handler(text='/binfo')
async def command_binfo(message: types.Message):
    await message.answer(f'<b>Учебная часть</b>\n'
                         f'<i>Власова Марина Михайловна (Директор):</i>\n'
                         f'mtk@mail.master-it.ru\n'
                         f'8 (812) 251-32-67\n'
                         f'<i>Щеглова Елена Васильевна (Заместитель директора по учебно-методической работе):</i>\n'
                         f'scheglova_ev@mtkspb.ru\n'
                         f'8 (812) 251-31-84\n'
                         f'<i>Кононова Елена Викторовна (Заведующий отделением Медицинская оптика (базовый уровень) и Лечебное дело):</i>\n'
                         f'elena.v.kononova@yandex.ru\n'
                         f'8 (812) 251-17-84\n'
                         f'<i>Савич Олеся Владимировна (Заведующий отделением Сестринское дело и Медицинская оптика (углубленный уровень)):</i>\n'
                         f'savich_ov@mtkspb.ru\n'
                         f'8 (812) 251-17-84\n'
                         f'<i>Калиберда Елена Сергеевна (Заведующий заочным отделением):</i>\n'
                         f'zaochnoe@mtkspb.ru\n'
                         f'8 (812) 251-17-84 \n'
                         f'<i>Красулина Светлана Анатольевна (Заведующий учебно-производственной практикой):</i>\n'
                         f'krasulina_sa@mtkspb.ru\n'
                         f'8 (812) 251-63-29\n'
                         f'<i>Николаенко Ольга Сергеевна (Специалист по трудоустройству):</i>\n'
                         f'nikolaenko_os@mtkspb.ru\n'
                         f'8 (812) 251-63-29\n'
                         f'<i>Харитонова Полина Григорьевна (Заведующий учебной частью):</i>\n'
                         f'edd@mtkspb.ru\n'
                         f'8 (812) 575-27-17\n'
                         f'<i>Соколова Анна Александровна (Секретарь учебной части):</i>\n'
                         f'edupart@mtkspb.ru\n'
                         f'(812) 575-27-17\n\n'
                         f'<b>Отдел по воспитательной работе</b>\n'
                         f'<i>Лисняк Марина Леонидовна (Начальник отдела по воспитательной работе):</i>\n'
                         f'lisniak_ml@mtkspb.ru\n'
                         f'8 (812) 251-52-66\n'
                         f'<i>Вилюкова Яна Валерьевна (Педагог-организатор):</i>\n'
                         f'vilukova_yv@mtkspb.ru\n'
                         f'8-982-212-77-67\n'
                         f'<i>Долгович Елена Борисовна (Социальный педагог):</i>\n'
                         f'dolgovich_eb@mtkspb.ru\n'
                         f'8 (812) 251-12-62\n'
                         f'<i>Змейков Максим Вячеславович (Педагог психолог):</i>\n'
                         f'sp@mtkspb.ru\n'
                         f'8 (812) 251-12-62\n'
                         f'<i>Гагарина Кристина Александровна (Заведующий библиотекой):</i>\n'
                         f'libr@mtkspb.ru\n'
                         f'8 (812) 251-32-67\n\n'
                         f'<b>Отдел кадров</b>\n'
                         f'<i>Трапша Яна Александровна (Начальник отдела кадров):</i>\n'
                         f'ok@mtkspb.ru\n'
                         f'8 (812) 251-95-69\n'
                         f'<i>Милованова Надежда Николаевна (Специалист по кадрам):</i>\n'
                         f'ok@mtkspb.ru\n'
                         f'8 (812) 251-95-69\n'
                         f'<i>Мельникова Валентина Алексеевна (Специалист по работе с иностранными студентами):</i>\n'
                         f'mtk@mail.master-it.ru\n'
                         f'8 (812) 251-32-67\n\n'
                         f'<b>Отдел бухгалтерского учета и отчетности</b>\n'
                         f'<i>Казанцева Анастасия Сергеевна (Главный бухгалтер):</i>\n'
                         f'buh@mtkspb.ru\n'
                         f'8 (812) 251-27-64\n'
                         f'<i>Корель Ольга Станиславовна (Заместитель главного бухгалтера):</i>\n'
                         f'buh@mtkspb.ru\n'
                         f'8 (812) 251-27-64\n'
                         f'<i>Артюхина Юлия Николаевна (Специалист по закупкам):</i>\n'
                         f'zakupki@mtkspb.ru\n'
                         f'8 (812) 251-27-64\n\n'
                         f'<b>Административно-хозяйственный отдел</b>\n'
                         f'<i>Солохина Наталья Витальевна (Начальник административно-хозяйственного отдела):</i>\n'
                         f'ahd@mtkspb.ru\n'
                         f'8 (812) 251-23-69\n\n'
                         f'<b>Отдел безопасности</b>\n'
                         f'<i>Давыденко Александр Сергеевич (Начальник отдела безопасности):</i>\n'
                         f'das01@list.ru\n'
                         f'8 (812) 251-45-63\n'
                         f'<i>Красненкова Мария Ивановна (Специалист по информационно-документационному обеспечению):</i>\n'
                         f'mariya@mtkspb.ru\n'
                         f'8 (812) 575-34-55\n'
                         f'<i>Андреев Виктор Васильевич (Системный администратор):</i>\n'
                         f'viktor@mtkspb.ru\n'
                         f'8 (812) 575-34-55\n\n'
                         f'<b>Отделение дополнительного образования</b>\n'
                         f'<i>Коняева Ольга Николаевна (Заведующий отделением дополнительного образования):</i>\n'
                         f'pk@mtkspb.ru\n'
                         f'opkmtk@mail.ru\n'
                         f'8 (812) 251-92-63\n'
                         f'<i>Колмагорова Юлия Михайловна (Специалист по дополнительному образованию):</i>\n'
                         f'pk@mtkspb.ru\n'
                         f'opkmtk@mail.ru\n'
                         f'8 (812) 251-92-63\n\n'
                         f'<b>Учебный салон оптики</b>\n'
                         f'<i>Смирнов Петр Михайлович (Заведующий учебным салоном оптики):</i>\n'
                         f'smirnov_pm@mtkspb.ru\n'
                         f'8 (812) 251-17-84\n\n'
                         f'<b>Общежитие</b>\n'
                         f'<i>Гузова Ирина Владимировна (Заведующий общежитием):</i>\n'
                         f'mtk@mail.master-it.ru\n'
                         f'8 (812) 450-68-95')