from typing import List

from aiogram import Dispatcher


class Notifier:
    def __init__(self, dp: Dispatcher, path_to_input_file: str, users_to_notify: List[str]):
        self._dp = dp
        self._file = path_to_input_file
        self._users = users_to_notify

    def _read_file(self) -> str:
        try:
            with open(self._file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            self._clear_file()

    def _clear_file(self):
        with open(self._file, 'w') as file:
            file.write("")

    async def check(self):
        message = self._read_file()
        if not message:
            return

        self._clear_file()

        for user in self._users:
            try:
                await self._dp.bot.send_message(user, message)
            except:
                pass

