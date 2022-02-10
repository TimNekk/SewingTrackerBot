from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import USERS_TO_NOTIFY
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.chat.id in USERS_TO_NOTIFY:
        text = "Привет, я буду отправлять уведомления, когда цена в магазинах будет ниже чем МРЦ"
    else:
        text = "Привет, если хочешь получать уведомления, напиши об этом @TimNekk"

    await message.answer(text)
