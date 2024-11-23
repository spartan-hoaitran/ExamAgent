from pydantic import BaseModel
from typing import Dict, List, Optional

class Question(BaseModel):
    question_type:str = "essay" # single_choice, multiple_choice, essay
    question:str = "What is await in Python?"
    options:Optional[List[str]] = []
    ai_answer: List[str]= ["Await is a keyword that is used to pause the execution of the asynchronous function until the promise is settled."]
    evaluation: Optional[Dict[str, str]] = None
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
    exam_id: str
    title: str
    description:str
    user_summary:str
    user_roadmap:List
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
