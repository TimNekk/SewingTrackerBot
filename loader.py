from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from data.config import INPUT_FILE, USERS_TO_NOTIFY, DB_PATH
from utils.Notifier import Notifier
from utils.db_api.sqlite import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(DB_PATH)

notifier = Notifier(dp, INPUT_FILE, USERS_TO_NOTIFY)
