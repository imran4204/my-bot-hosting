import os
from fastapi import FastAPI, Request
import uvicorn
import requests

app = FastAPI()

TOKEN = "8917550024:AAEX8uCZT_ZhhfZLTorolZAwCQU-5zjlBlY"
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

@app.get("/")
def home():
    return {"status": "Bot Server is running!"}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        if text == "/start":
            reply_text = "হ্যালো! সফলভাবে রেন্ডার থেকে আপনার বট কানেক্ট হয়েছে!"
        else:
            reply_text = f"আপনার মেসেজ পেয়েছি: {text}"
            
        url = f"{TELEGRAM_API}/sendMessage"
        payload = {"chat_id": chat_id, "text": reply_text}
        requests.post(url, json=payload)
        
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
