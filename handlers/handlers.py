from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter
from database.requests import *
import os
from database.models import *

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import keyboards.keyboards as kb

router = Router()


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == int(os.getenv('ADMIN_ID'))


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAEBPPllFdFBeCkiCCt2glfEsYSis9BlvgAC3AUAAj-VzArxX-zMZBcVlzAE')
    await message.answer(f'{message.from_user.first_name}, привет от Дианы 💕',
                         reply_markup=kb.main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=kb.admin)


@router.message(F.text == '🤷‍♀️ Помощь')
async def sos(message: Message):
    await message.answer('Выберите категорию', reply_markup=kb.sos)


@router.message(F.text == '💅 Запись')
async def echo(message: Message):
    await message.answer('Доступное время для записи', reply_markup=await kb.free_records())


@router.callback_query(F.data == 'Telegram')
async def telegram(callback: CallbackQuery):
    await callback.message.answer(f'Вы выбрали {callback.data}')


@router.callback_query(F.data.startswith('book_'))
async def select_date(callback: CallbackQuery):
    try:
        _, day, month, year, hour, minute = callback.data.split('_')
    except Exception:
        return
    print(day, month, year, hour, minute)
    print(callback.message.from_user.id)





