from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN","")
BOT_NAME = getenv("BOT_NAME","⛧𓆩🖤 BROKEN MR Z 𝗠𝗨𝗦𝗜𝗖 🖤𓆪⛧")
BOT_USERNAME = getenv("BOT_USERNAME", "broken_mr_z_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "iam_your_heart4")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "200"))
SESSION_NAME = getenv("SESSION_NAME", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "• / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2082934030").split()))
