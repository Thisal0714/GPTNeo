

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
    "Authorization": "Bearer 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"
}

class TextRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(req: TextRequest):
    payload = {"inputs": req.prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    
    res_json = response.json()
    
    # Check if response contains error key
    if "error" in res_json:
        return {"error": res_json["error"]}
    
    generated = res_json[0]["generated_text"]
    return {"result": generated}


