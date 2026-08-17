import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# আপনার টোকেন
TOKEN = "8917550024:AAEX8uCZT_ZhhfZLTorolZAwCQU-5zjlBlY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('হ্যালো! আমি আপনার বটের কন্ট্রোল প্যানেল। আমি এখন কাজ করছি!')

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
