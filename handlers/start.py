from pyrogram import Client as Yonebot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Yonebot.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start_(client: Yonebot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {message.from_user.first_name}![🤓](https://telegra.ph/file/fe77d94e2105721ce4353.jpg)
        
I am 𝐘𝐨𝐧𝐞 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭🎶🎸

I can play songs in your group's VC [🤗](https://telegra.ph/file/fe77d94e2105721ce4353.jpg)

To listen songs add me to your group..

And don't forgot to promote me with all rights![🥰](https://telegra.ph/file/fe77d94e2105721ce4353.jpg)

Otherwise I can't play songs!🥺👉[👈](https://telegra.ph/file/fe77d94e2105721ce4353.jpg)

Use the buttons below to know more about me..😊
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "⚡Commands⚡", url="https://telegra.ph/commands-06-14-2")
                  ],[
                    InlineKeyboardButton(
                        "😎Owner😎", url="https://t.me/H1M4N5HU0P"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🔥Support Group🔥", url="https://t.me/KoraSupport"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Yonebot.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(client: Yonebot, message: Message):
      await message.reply_text("""**𝐘𝐨𝐧𝐞 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭🎶🎸 is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😎Owner😎", url="https://t.me/H1M4N5HU0P")
                ]
            ]
        )
   )

