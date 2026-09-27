AI API using FastAPI and Ollama

Introduction

This is my Day 1 GenAI internship project.
In this project, I created a simple API using FastAPI and connected it with the Qwen3 LLM using Ollama.
The user can send a question to the API, and the API sends the question to Qwen3. The generated answer is then returned to the user.

What I Learned

In this project, I learned about:

- What is an API
- What is a REST API
- GET and POST methods
- Request and Response
- JSON
- API endpoints
- FastAPI
- Uvicorn
- Ollama
- How to connect an LLM with FastAPI
- How an API sends a request and returns a response

Technologies Used

- Python
- FastAPI
- Uvicorn
- Ollama
- Qwen3
- Requests
- JSON
- Swagger UI


Project Work Flow

User
↓
POST /generate
↓
FastAPI
↓
Ollama API
↓
Qwen3 LLM
↓
Generated Answer
↓
FastAPI
↓
JSON Response
↓
User
