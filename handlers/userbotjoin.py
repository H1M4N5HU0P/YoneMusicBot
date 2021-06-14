from callsmusic.callsmusic import client as Yonemusic
from pyrogram import Client as Yonebot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Yonebot.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Add me as admin of yor group first</b>",
        )
        return

    try:
        user = await Yonemusic.get_me()
    except:
        user.first_name =  "𝐘𝐨𝐧𝐞 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭🎶🎸"

    try:
        await Yonemusic.join_chat(invitelink)
        await Yonemusic.send_message(message.chat.id,"I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your chat</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your group due to heavy join requests for userbot! Make sure user is not banned in group."
            "\n\nOr manually add @YoneMusic_bot to your Group and try again</b>",
        )
        return
    await message.reply_text(
            "<b>helper userbot joined your chat</b>",
        )
    
@Yonemusic.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(Yonemusic, message):
    try:
        await Yonemusic.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>User couldn't leave your group! May be floodwaits."
            "\n\nOr manually kick me from to your Group</b>",
        )
        return
