from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hey {format(
        message.from_user.mention)}!
I am 𝐘𝐨𝐧𝐞 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭🎶🎸
I can play songs in your group's VC [😉](https://telegra.ph/file/fe77d94e2105721ce4353.jpg)

To listen songs add me to your group..

And don't forgot to promote me with all rights!😉
Otherwise I can't play songs!🥺👉👈

Use the buttons below to know more about me..🔥
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Group❤️", url="https://t.me/KoraSupport",
                    )
                ],
                [    
                    InlineKeyboardButton(
                        text="Commands🥰", callback_data="help"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/YoneMusic_bot?startgroup=true"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""🎶How To Use Yone Music Bot Explained Below Read Carefully!👇👇

First Of All add this bot in your groups And make admin to work properly🎸

The commands and there use is explained here:-

1./saavn To search song on jio saavan and play the first result

2./play song name To search the song on Youtube and play the first matching result(you can play yt link too).

3./song Reply this in response to a any telegram audio file it will be played

4./skip to skip current song

5./end to stop the streaming of song

6./pause to pause the strea

7./resume to resume the playback.

8.Inline search is also supported.

📌Note= Sometime it works without admin rights but sometime it doesn't works so make admin to both the bots to work properly🤗

Support Group:- @KoraSupport"""
