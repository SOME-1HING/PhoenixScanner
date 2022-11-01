import os
from PhoenixScanner import Phoenix
from .. import pbot as RedSeven 
from pyrogram.types import Message
from pyrogram import filters

RED = Phoenix(os.getenv("RED7_TOKEN"))
SCANLIST = []

@RedSeven.on_message(filters.text & filters.user(5483120234))
async def update_list(bot: RedSeven, message: Message):
    global SCANLIST
    newlist = RED.scanlist()
    if newlist == {'message': 'Invalid Token'}:
        newlist = RED.scanlist()
        if newlist == {'message': 'Invalid Token'}:
            raise 'Invalid Scanner Token'
    SCANLIST = newlist
    await message.reply_text(f"Scanlist Updated.\nScanned users: `{SCANLIST}`")
    

@RedSeven.on_message(filters.group & filters.all)
async def red7xphoenix(bot: RedSeven, message: Message):
   user = message.from_user
   chat = message.chat
   
   if user.id in SCANLIST:
      user = await bot.get_users(user.id)
      msg = f"""
 **Alert ⚠️**
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
