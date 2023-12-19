from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.requests import get_free_records
import locale


locale.setlocale(locale.LC_TIME, 'ru_RU')


main_kb = [
    [KeyboardButton(text='💅 Запись'),
     KeyboardButton(text='💸 Прайс')],
    [KeyboardButton(text='💕 Мой профиль '),
     KeyboardButton(text='🤷‍♀️ Помощь')]
]

admin_kb = [
    [KeyboardButton(text='Изменить запись'),
     KeyboardButton(text='Свободные окна')],
    [KeyboardButton(text='Создать график'),
     KeyboardButton(text='Подтвердить запись')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

admin = ReplyKeyboardMarkup(keyboard=admin_kb,
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт ниже')

sos = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Telegram', callback_data='Telegram')],
    [InlineKeyboardButton(text='Instagram', callback_data='Instagram')]
])


async def free_records():
    free_records_kb = InlineKeyboardBuilder()
    records = await get_free_records()
    for record in records:
        cdate = record.strftime('%d_%m_%Y_%H_%M')
        free_records_kb.add(InlineKeyboardButton(text=record.strftime('%d.%m %a %H:%M'), callback_data=f'book_{cdate}'))
    return free_records_kb.adjust(2).as_markup()




