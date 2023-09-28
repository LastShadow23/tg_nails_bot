from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter

import keyboards.keyboards as kb

router = Router()


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [460219354]


@router.message(Admin(), F.text == '/admin')
async def cmd_admin(message: Message):
    await message.answer('Вы админ.')


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=kb.main)


@router.message(F.text == '🤷‍♀️ Помощь')
async def sos(message: Message):
    await message.answer('Выберите категорию', reply_markup=kb.sos)


@router.callback_query(F.data == 'Telegram')
async def telegram(callback: CallbackQuery):
    await callback.message.answer(f'Вы выбрали {callback.data}')


@router.message()
async def echo(message: Message):
    await message.answer('Я тебя не понимаю...')
