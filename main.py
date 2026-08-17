from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Server is running perfectly!"}

@app.post("/run-bot")
def run_bot(token: str):
    return {"status": "Bot configuration received", "token_preview": token[:5] + "..."}
