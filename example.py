import os
from pyrogram import Client, filters
from pyrogram.types import Message
from PhoenixScanner import Phoenix

RED = Phoenix(os.getenv("RED7_TOKEN"))

@Message.on_message(filters.group & filters.all)
async def red7xphoenix(bot: Client, message: Message):
   user = message.from_user
   chat = message.chat
   
   check = RED.check(user.id)
   if check['is_gban']:
      try:
         user = await bot.get_users(user.id)
         msg = f"""
** Alert ⚠️**
User [{user.first_name}](tg://user?id={user.id}) is officially
Scanned by Team Red7 | Phoenix API ;)

Appeal [Here](https://t.me/Red7WatchSupport)
"""
         await bot.ban_chat_member(user.id)
         await bot.send_message(chat.id, msg)
      except:
         await bot.send_message(chat.id, msg)
         pass
