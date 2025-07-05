

# fastapi_gptneo.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Read token from env variable (best practice!)
HF_API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

class TextRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(req: TextRequest):
    payload = {"inputs": req.prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": response.json()}
    
    generated = response.json()[0]["generated_text"]
    return {"result": generated}

