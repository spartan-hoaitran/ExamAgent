from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, List, Optional

router = APIRouter()
# Define data models

class Question(BaseModel):
    question_type:str = "essay" # single_choice, multiple_choice, essay
    question:str = "What is await in Python?"
    options:Optional[List[str]] = []
    ai_answer: List[str]= ["Await is a keyword that is used to pause the execution of the asynchronous function until the promise is settled."]
    evaluation: Optional[Dict[str, str]] = None
    score: Optional[int] = None
    
class InputCreateExam(BaseModel):
    exam_id: str
    title: str
    doc_id: List[str]
    file_upload: List[str] # List of file paths or URLs
    ratio_question: Dict[str, float] = { "single_choice":0.3 ,"multiple_choice": 0.4, "essay": 0.3}

    
class Exam(BaseModel):
    exam_id:str
    title: str
    questions: List[Question]
    
class ExamSubmission(BaseModel):
    exam_id: str
    questions: List[Question]
    answers: List[str]
    
class ExamResult(BaseModel):
    exam_id: str
    questions: List[Question]
    total_score: int
    feedback: str


# Create an exam
@router.post("/create_exams/", response_model=Exam)
async def create_exam(input_create_exam: InputCreateExam):
    # Generate questions based on the input
    # For simplicity, we'll just return a dummy exam
    questions = [
        {
            "question_type": "single_choice",
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_option": 2,
        },
        {
            "question_type": "multiple_choice",
            "question": "Which programming languages are commonly used for web development?",
            "options": ["Java", "Python", "JavaScript", "C++"],
            "correct_options": [2, 3],
        },
        {
            "question_type": "essay",
            "question": "Explain the concept of recursion in programming.",
            "ai_answer": ["Recursion is a programming concept where a function calls itself to solve a problem."],
        },
    ]

    exam = Exam(
        exam_id= input_create_exam.exam_id,
        title=input_create_exam.title,
        questions= questions
    )

    return exam


# Evaluate an exam submission
@router.post("/exams/evaluate/", response_model=ExamResult)
async def evaluate_exam(submission: ExamSubmission):
    # For simplicity, we'll just return a dummy result
    total_score = 0
    
    result=ExamResult(exam_id=submission.exam_id, questions=submission.questions, total_score=total_score, feedback="Well done!")
    return result