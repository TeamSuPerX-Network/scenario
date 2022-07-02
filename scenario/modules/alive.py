""" Alive module from https://github.com/AnonymousR1025/FallenRobot/blob/55c53a2f37f4062c63265375a7ca19b9a507afcd/FallenRobot/modules/alive.py"""

import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from scenario.events import register
from scenario import telethn as tbot
from scenario import SUPPORT_CHAT


PHOTO = [
    "https://telegra.ph/file/315d78ebea36b0a1b3435.jpg",
    "https://telegra.ph/file/7bd111132fce009e4605e.jpg",
    "https://telegra.ph/file/804a5f9a3c32bac1ae15c.jpg",
    "https://telegra.ph/file/43edaa8914b7ce8998336.jpg",
    "https://telegra.ph/file/abed92d9b3ff409793324.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nI Aᴍ Siyana~**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ​ : [Sh4adow](https://t.me/Unknown_SH4DOW_xD)** \n\n"
  TEXT += f"» **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("💻 Տᴜᴘᴘᴏʀᴛ​", "t.me/Siyana_support"), Button.url("ႮᴘᴅᴀᴛᴇՏ 💻​", f"https://t.me/Siyana_Updates")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

__help__ = """
/repo - Get repo
/alive - Alive status
"""

__mod_name__ = "Alive"
