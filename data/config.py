from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMIN = env.str("ADMIN")
USERS_TO_NOTIFY = env.list("USERS_TO_NOTIFY")
IP = env.str("ip")

