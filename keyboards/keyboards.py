from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

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
