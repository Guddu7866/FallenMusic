from pyrogram import Client
import asyncio
from config import SUDO_USERS, BOT_NAME, BOT_USERNAME
from config import PMPERMIT, OWNER_USERNAME
from pyrogram import filters
from pyrogram.types import Message
from callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "ʜᴇʏ {},\nᴛʜɪs ɪs [{}](t.me{}) ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ʙᴀʙʏ.\n\nᴅᴏɴ'ᴛ sᴘᴀᴍ ʜᴇʀᴇ ʙᴀʙʏ PLEASE CONTACT HERE OWNER 😘[BROKEN MR Z](t.me/iam_your_heart4).\n".format(
          message.from_user.mention, BOT_NAME, BOT_USERNAME, OWNER_USERNAME ),
            )
            return

    

@Client.on_message(filters.command(["!pm"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("ᴘᴍ ᴘᴇʀᴍɪᴛ ᴇɴᴀʙʟᴇᴅ ʙᴀʙʏ")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("ᴘᴍ ᴘᴇʀᴍɪᴛ ᴅɪsᴀʙʟᴇᴅ ʙᴀʙʏ")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ​ ʙᴀʙʏ")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", ["!", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ​")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", ["!", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("ᴅɪsᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ​")
        return
    message.continue_propagation()
