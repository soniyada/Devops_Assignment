from fastapi import FastAPI
import requests

app = FastAPI()

WORKER_URL = "http://10.0.1.10:8000/infer"

@app.post("/api/infer")
def infer(data: dict):
    text = data["text"]

    response = requests.get(WORKER_URL, params={"text": text})

    return response.json()


RUN

uvicorn gateway:app --host 0.0.0.0 --port 80
