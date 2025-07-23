from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import random

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

APP_NAME = os.getenv("APP_NAME", "QuizAPI")

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "What is the capital of France?",
        "options": ["Paris", "Madrid", "Berlin", "London"],
        "answer": "Paris"
    },
    {
        "id": 2,
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Shakespeare", "Hemingway", "Dickens", "Orwell"],
        "answer": "Shakespeare"
    },
    {
        "id": 3,
        "question": "Which planet is closest to the Sun?",
        "options": ["Mercury", "Venus", "Earth", "Mars"],
        "answer": "Mercury"
    },
]

@app.get("/")
def root():
    return {"message": f"Welcome to {APP_NAME}!"}

@app.get("/api/question")
def get_question():
    q = random.choice(QUIZ_QUESTIONS)
    return {
        "id": q["id"],
        "question": q["question"],
        "options": q["options"]
    }

@app.get("/api/check")
def check_answer(id: int = Query(...), selected: str = Query(...)):
    for q in QUIZ_QUESTIONS:
        if q["id"] == id:
            is_correct = (q["answer"].lower() == selected.lower())
            return {"correct": is_correct, "answer": q["answer"]}
    return {"error": "Invalid question ID"}
