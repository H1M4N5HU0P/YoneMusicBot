from pyrogram import Client as Yonebot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


Yonebot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

Yonebot.start()
run()
