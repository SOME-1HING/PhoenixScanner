import os
from pyrogram import Client, filters
from pyrogram.types import Message
from PhoenixScanner import Phoenix
from .. import pbot as RedSeven 


if os.getenv("RED7_TOKEN", None):
    RED7_TOKEN = os.getenv("RED7_TOKEN")
else:
    try:
        from configparser import ConfigParser
        p = ConfigParser()
        p.read("config.ini")
        RED7_TOKEN = p.get("int.py", "RED7_TOKEN")
    except:
        try:
            from ..config import Development as Config
            RED7_TOKEN = Config.RED7_TOKEN
        except:
            RED7_TOKEN = None
if RED7_TOKEN and __name__.split(".")[-1] in ALL_MODULES:

    try:

        RED = Phoenix(RED7_TOKEN)

        LOGGER.info("Connection established successfully.")

    except Exception as e:

        RED = None

        LOGGER.error(

            f"Failed to load Reason:- /n {e.with_traceback(e.__traceback__)}",

        )

else:

    LOGGER.info("RED7 module not loaded! ")




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
