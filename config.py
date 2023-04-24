from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "7748505"))
API_HASH = getenv("API_HASH", "0cce05579998b3bb6e99058052a1c0b1")

BOT_TOKEN = getenv("BOT_TOKEN", "6051877221:AAGzNwGUmFOQEszigPvk01TpGqP5fQxofgI")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "161882596"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BAB2O5kAgm-CmZsbff4LSsfjAVd4t4xMSVGKN7eB5H5hIX_XcQzdvwBayRkVr4NsS6gnEVQqUVm-SVwz3m5jZHpnnEoc2A9BNqejcFIqnvFw9jBm1j0UJZd7JE7swr6y21qnzLc_sViqYJSqndsd8cnNtXtdsI3B-7gdtnkg5yh56p8e2SrtY_OqiG-tS38b99sMTa_vVyKr2Yby3UIi-2dEt7cJOa4tPlqE75JjJV-on5EErMQg9tsLFOFenuMvJvFa1fGSAQiya3OGfTfQ8dQSeI8iZyxFyOdIJxVQttBUHCqdjzfLpYTdEnOOngd8YGolVIsStC2Vw7KZa3aOUvHlEVbrtwAAAAAJpiHkAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/beeeeeee007")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kosssshheeeeeeerrrrrr")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "161882596").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
