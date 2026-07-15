from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("8998165908:AAEmAgc1LTp2YAondi30GMFGzpIjqwS9dw8")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Welcome to TBCoin Mining Bot!\n\n"
        "⛏️ আপনার অ্যাকাউন্ট সফলভাবে তৈরি হয়েছে।"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
