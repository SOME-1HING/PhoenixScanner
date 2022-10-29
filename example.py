[In reply to SOME1HING]
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from PhoenixScanner import Phoenix
from .. import pbot as RedSeven 


RED = Phoenix(os.getenv("RED7_TOKEN"))

@RedSeven.on_message(filters.group & filters.all)
async def red7xphoenix(bot: RedSeven, message: Message):
   user = message.from_user
   chat = message.chat
   
   check = RED.check(user.id)
   if check['is_gban']:
      user = await bot.get_users(user.id)
      msg = f"""
 Alert ⚠️
User [{user.first_name}](tg://user?id={user.id}) is officially
Scanned by Team Red7 | Phoenix API ;)

Appeal [Here](https://t.me/Red7WatchSupport)
"""
      try:
         await bot.ban_chat_member(chat.id, user.id)
         await bot.send_message(chat.id, msg, disable_web_page_preview=True)
      except:
         await bot.send_message(chat.id, msg, disable_web_page_preview=True)
         pass
