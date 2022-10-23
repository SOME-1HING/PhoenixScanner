from Phoenix import Phoenix

from telegram import Update
from telegram.ext import (
    CallbackContext,
    Filters,
    MessageHandler,
)

from Bot import dispatcher
from Bot import DRAGONS
from Bot.modules.sql import global_bans_sql as sql

scanner = Phoenix()

def phoenix(update: Update, context: CallbackContext):
    msg = update.effective_message
    user = msg.from_user

    if user.id in DRAGONS:
        return
    
    is_gban, reason = scanner.gban_check(user.id)
    
    if is_gban:
        sql.gban_user(user.id, user.username or user.first_name, reason)
        update.effective_message.reply_text(f"""
# SCANNED
User ID: {user.id}
Reason: {reason}
        """)
        
dispatcher.add_handler(MessageHandler(Filters.all & Filters.chat_type.groups, phoenix, run_async = True))
