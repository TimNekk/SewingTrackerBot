from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMIN = env.str("ADMIN")
USERS_TO_NOTIFY = list(map(int, env.list("USERS_TO_NOTIFY")))
IP = env.str("ip")
INPUT_FILE = env.str("INPUT_FILE")
DB_PATH = env.str("DB")

