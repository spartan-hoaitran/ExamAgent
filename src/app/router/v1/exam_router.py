from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class InputCreateExam(BaseModel):
    exam_id: str
    title: str
    
# Define data models
class Question(BaseModel):
    question_text: str
    options: List[str]
    correct_option: int

class Exam(BaseModel):
    exam_id:str
    title: str
    questions: List[Question]
    

class ExamSubmission(BaseModel):
    exam_id: int
    answers: List[int]


# In-memory storage for simplicity
exams_db = []
submissions_db = []

# Create an exam
@router.post("/exams/", response_model=Exam)
async def create_exam(exam: Exam):
    exam_id = len(exams_db) + 1
    exams_db.append({"id": exam_id, **exam.dict()})
    return exam_id

# Evaluate an exam submission
@router.post("/exams/{exam_id}/evaluate/")
async def evaluate_exam(exam_id: int, submission: ExamSubmission):
    if exam_id > len(exams_db) or exam_id <= 0:
        raise HTTPException(status_code=404, detail="Exam not found")

    exam = exams_db[exam_id - 1]
    correct_answers = sum(
        1 for question, answer in zip(exam['questions'], submission.answers)
        if question['correct_option'] == answer
    )
    score = correct_answers / len(exam['questions']) * 100
    submissions_db.append({"exam_id": exam_id, "score": score})
    return {"score": score}

