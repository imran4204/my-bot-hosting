import os
import threading
from fastapi import FastAPI
import uvicorn
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# FastAPI সার্ভার সেটআপ (রেন্ডারকে খুশি রাখার জন্য)
app = FastAPI()

@app.get("/")
def home():
    return {"status": "Telegram Bot & Web Server is running live!"}

# টেলিগ্রাম বটের কমান্ড হ্যান্ডলার
TOKEN = "8917550024:AAEX8uCZT_ZhhfZLTorolZAwCQU-5zjlBlY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('হ্যালো! আমি আপনার বট, এখন সফলভাবে রেন্ডার থেকে লাইভ আছি!')

def run_telegram_bot():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()

# ব্যাকগ্রাউন্ডে টেলিগ্রাম বট চালু করার জন্য থ্রেড
if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_telegram_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # ওয়েব সার্ভার রান করা
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
