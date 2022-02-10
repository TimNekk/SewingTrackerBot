import asyncio

import aioschedule
from aiogram import executor

from loader import dp, notifier
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def scheduler():
    aioschedule.every().minute.do(notifier.check)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dispatcher):
    # Create Scheduler
    asyncio.create_task(scheduler())

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

