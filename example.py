from PhoenixScanner import Phoenix

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
    
    is_gban, reason, scannedby = scanner.gban_check(user.id)
    res = f"{reason}. Scanned by: {scannedby}"
    
    if is_gban:
        sql.gban_user(user.id, user.username or user.first_name, res)
        update.effective_message.reply_text(f"""
# SCANNED
User ID: {user.id}
Reason: {reason}
Scanned By: {scannedby}
        """)
        
dispatcher.add_handler(MessageHandler(Filters.all & Filters.chat_type.groups, phoenix, run_async = True))
