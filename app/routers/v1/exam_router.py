from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, List, Optional
from services.exam_service import ExamService
from schemas.exam_schemas import Exam, ExamResult, ExamSubmission, InputCreateExam
router = APIRouter()

# Create an exam
# @router.post("/create_exams/", response_model=Exam)
# def create_exam(input_create_exam: InputCreateExam):
#     # Generate questions based on the input
#     # For simplicity, we'll just return a dummy exam
#     questions = [
#         {
#             "question_type": "single_choice",
#             "question": "What is the capital of France?",
#             "options": ["Berlin", "Madrid", "Paris", "Rome"],
#             "correct_option": 2,
#         },
#         {
#             "question_type": "multiple_choice",
#             "question": "Which programming languages are commonly used for web development?",
#             "options": ["Java", "Python", "JavaScript", "C++"],
#             "correct_options": [2, 3],
#         },
#         {
#             "question_type": "essay",
#             "question": "Explain the concept of recursion in programming.",
#             "ai_answer": ["Recursion is a programming concept where a function calls itself to solve a problem."],
#         },
#     ]

#     exam = Exam(
#         exam_id= input_create_exam.exam_id,
#         title=input_create_exam.title,
#         questions= questions
#     )

#     return exam

# Create an exam
@router.post("/exams/create/", response_model=Exam)
def create_exam(input_create_exam: InputCreateExam):
    # Generate questions based on the input
    # For simplicity, we'll just return a dummy exam
    print("Request from create_exams:",input_create_exam)
    exam_service= ExamService()
    questions=exam_service.create_exam_handler(input_create_exam)
    print("Response for create_exams:",questions)
    return Exam(
        questions= questions
    )



# Evaluate an exam submission
# @router.post("/exams/evaluate/", response_model=ExamResult)
@router.post("/exams/evaluate/")
def evaluate_exam(submission: ExamSubmission):
    print("Request from /exams/evaluate/:",submission)
    exam_service=ExamService()
    results=exam_service.evaluate_exam_handler(submission)
    print("Response for /exams/evaluate/",results)
    return results