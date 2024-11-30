from pydantic import BaseModel
from typing import Dict, List, Optional

class Question(BaseModel):
    question_type:str = "essay" # single_choice, multiple_choice, essay
    question:str = "What is in Python?"
    options:Optional[List[str]] = []
    ai_answer: Optional[List[str]]= ["is a keyword that is used to pause the execution of the asynchronous function until the promise is settled."]
    user_answer: Optional[List[str]]= []
    evaluation: Optional[str] = None
    score: Optional[int] = None
    
class InputCreateExam(BaseModel):
    """_summary_
        exam_id: str
    title: str
    file_upload: List[str] # List of file paths or URLs
    ratio_question: Dict[str, float] = { "single_choice":0.3 ,"multiple_choice": 0.4, "essay": 0.3}
    Args:
        BaseModel (_type_): _description_
    """
    description:str
    user_summary:str
    user_roadmap:str
    file_upload: List[str] # List of file paths or URLs
    ratio_question: Dict[str, float] = { "single_choice":0.3 ,"multiple_choice": 0.4, "essay": 0.3}
    total_question:int
    
class Exam(BaseModel):
    questions: List[Question]
    
class ExamSubmission(BaseModel):
    exam: List[Question]
    
class ExamResult(BaseModel):
    questions: List[Question]
    total_score: int
    feedback: str
