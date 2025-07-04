from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

ssummarizer = pipeline("text-generation", model="gpt2")

class SummarizeRequest(BaseModel):
    text: str

@app.post("/summarize")
async def summarize(req: SummarizeRequest):
    prompt = f"Summarize the following content in bullet points:\n{req.text}"
    result = summarizer(prompt, max_length=150, do_sample=True, temperature=0.7)
    return {"summary": result[0]['generated_text']}
