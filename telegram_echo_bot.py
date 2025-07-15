# telegram_echo_bot.py

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "7931865563:AAG1NAfPBWXK4xj-ajfAk3ue7KCJHYRkUNc"

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply = f"Hello! You wrote: {user_message}"
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

print("The bot is running. To stop it, click Ctrl+C")
app.run_polling()
