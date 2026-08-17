from fastapi import FastAPI
import docker
import os

app = FastAPI()
client = docker.from_env()

@app.get("/")
def home():
    return {"status": "Server is running!"}

@app.post("/run-bot")
def run_bot(token: str):
    container = client.containers.run(
        "python:3.10-slim",
        command=f"python -c \"import time; print('Bot Started'); time.sleep(86400)\"",
        detach=True
    )
    return {"status": "Bot started", "id": container.short_id}
