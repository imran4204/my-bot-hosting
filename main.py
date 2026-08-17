from fastapi import FastAPI, Request
import requests

app = FastAPI()

TELEGRAM_TOKEN = "8917550024:AAEX8uCZT_ZhhfZLTorolZAwCQU-5zjlBlY"
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.get("/")
def home():
    return {"status": "Telegram Bot & App Control Server is running successfully!"}

@app.post("/send-command")
def send_command(chat_id: str, message: str):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, json=payload)
    return {"status": "Command sent to Telegram bot", "telegram_response": response.json()}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    return {"status": "Webhook received"}
