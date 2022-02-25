from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import USERS_TO_NOTIFY, ADMIN


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.id is ADMIN

