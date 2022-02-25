import json
from pprint import pformat


from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hcode

from filters import IsWhitelisted
from handlers.users.models import get_history
from loader import dp, db


@dp.message_handler(IsWhitelisted(), CommandStart())
async def bot_start(message: types.Message):
    if not message.get_args():
        text = "<i>Привет, я буду отправлять уведомления, когда цена в магазинах будет ниже чем МРЦ</i>"
        await message.answer(text)
        return

    args = message.get_args().split("_")

    try:
        if args[0] == "history":
            model_name, market = args[1].replace("-", " "), args[2]
            model = db.get_model(model_name)
            text = await get_history(model, market)
        else:
            raise ValueError(f'"{args[0]}" mode not found')

        await message.answer(text)
    except Exception as e:
        await message.answer(f'Не удалось сериализировать deeplink\n\n{hcode(pformat(message.get_args()))}\n\n{hcode(e)}')
