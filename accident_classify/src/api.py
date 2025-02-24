import pickle
from fastapi import FastAPI
from core import main

app = FastAPI()

@app.get("/health")
async def health_check():
    return {
        "status":"ok"
    }

@app.post("/api")
async def accident_classify(sentence: str = "นาย A ขับรถชนนาย B"):
    x = main(sentence)
    results = {
        "sentence":sentence,
        "proba":x[0],
        "argmax":x[1],
        "class":x[2]
    }
    return results





