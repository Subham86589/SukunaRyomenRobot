from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as o
from telethon import __version__ as s

from FallenRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, pbot


@pbot.on_message(filters.command(["repo", "source"]))
async def repo(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**ʜᴇʏ {message.from_user.mention},

ɪ ᴀᴍ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ :** 𝐋𝐎𝐑𝐃 𝐒𝐔𝐁𝐁𝐔⚡
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑⚡", user_id=OWNER_ID),
                    InlineKeyboardButton(
                        "𝐊𝐍𝐎𝐖 𝐒𝐔𝐁𝐁𝐔⚡",
                        url="https://t.me/hewasSUBBU",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
