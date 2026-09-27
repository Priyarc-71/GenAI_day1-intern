from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return{
        "message" : "hi i am your api"
    }
@app.post("/generate")
def generate(request: PromptRequest):

    ollama_url = "http://localhost:11434/api/generate"
    data = {
        "model": "qwen3:4b",
        "prompt": "Answer only in English.\n" + request.prompt,
        "stream": False
    }

    response = requests.post(
        ollama_url,
        json=data
    )

    result = response.json()

    return {
        "response": result["response"]
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "Fstapi:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )