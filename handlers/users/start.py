from loader import dp
from aiogram import types


@dp.message_handler()
async def start(message: types.Message):
    await message.answer('Привет')

