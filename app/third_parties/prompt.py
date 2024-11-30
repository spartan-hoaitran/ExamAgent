CREATE_QUESTION_GPT="""You need to create {{number_of_questions}} of {{question_type}} question. Please follow the given information:
1 - The question should be followed the rules is given below:
{{rule}}
2 - The question must be about the documents:{{document}}.
Output format: [{"question":"string","choices":["string"],"correct_answer":["string"]}]
"""

CREATE_QUESTION_GEMINI=""""""
Doc="""A Question Answering and Quiz Generation Chatbot for Education\nSreelakshmi A.S. Department of Computer Science and Engineering National Institute of Technology, Tiruchirappalli Tamil Nadu, India sreelakshmias97@gmail.com Aishwarya Nair Department of Computer Science and Engineering National Institute of Technology, Tiruchirappalli Tamil Nadu, India aishwarya05nair@gmail.com\nAbstract-In recent years, there have been a number of chatbots developed in the field of education. While many of them are designed to answer queries based on publicly available information such as in community answering platforms, or from a predefined knowledge base, there is no possibility of customizing the information to be queried. Moreover, there are no existing chatbots capable of generating self assessment quizzes based on any given document. This paper proposes a Question Answering and Quiz Generation Chatbot that allows a user to upload relevant documents and perform two main functions on them, namely answer extraction and question generation. The uploaded document is converted into a knowledge base through a number of data cleaning and preprocessing steps. The Question Answering module uses ranking functions and neural networks to extract the most appropriate answer from the knowledge base and the Quiz Generation module identifies key sentences and generates question-answer pairs, which can be used to generate a quiz for the user.\nIndex Terms-Question Answering, Question Generation, Ar- tificial Neural Networks (ANN), Text ranking, MS MARCO dataset, Stanford Coref Annotator.\nI. INTRODUCTION\nA chatbot is a software used to imitate human conversation through text chats and voice commands. In recent times, chatbots have become increasingly popular, with a number of instant messaging services launching support for chatbots, making it very convenient to create chatbots for a number of applications. The developments in the field of NLP have lead to a growth in the number of intelligent tutoring """
QUESTION_FORMATTER="""Format input to question json object format :
Result:
[{"question":"string","choices":[],"correct_answer":["string"]}]
--------------------------------

Input: {{input}}
Result:
"""
EVALUATE_EXAM_GPT="""You need to evaluate the exam submission. Give feedback for each question in field "evaluation". And give score for each question in field "score" based on 5-point grading scale. The overall of all questions feedback should be in field "feedback". 
Example:
{"exam": [{
            question_type="essay",
            question="What is in Python?",
            ai_answer=["is a keyword that is used to pause the execution of the asynchronous function until the promise is settled."],
            user_answer=["is used to pause the execution of functions."],  # Mistake: missing the "until the promise is settled" part
            evaluation="",
            score=0
        },
        {
            question_type="single_choice",
            question="Which of the following is the correct way to define a function in Python?",
            options=["def my_func():", "function my_func():", "func my_func():"],
            ai_answer=["def my_func():"],
            user_answer=["function my_func():"],  # Mistake: incorrect syntax
            evaluation="",
            score=0
        },
        {
            question_type="multiple_choice",
            question="What are the valid data types in Python?",
            options=["int", "string", "boolean", "number"],
            ai_answer=["int", "string", "boolean"],
            user_answer=["int", "number"],  # Mistake: 'number' is not a valid data type in Python
            evaluation="",
            score=0
        }]
}
Result:
{"exam": [{
            question_type="essay",
            question="What is in Python?",
            ai_answer=["is a keyword that is used to pause the execution of the asynchronous function until the promise is settled."],
            user_answer=["is used to pause the execution of functions."],  # Mistake: missing the "until the promise is settled" part
            evaluation="The answer is partially correct. The complete explanation includes the promise settling part.",
            score=5
        },
        {
            question_type="single_choice",
            question="Which of the following is the correct way to define a function in Python?",
            options=["def my_func():", "function my_func():", "func my_func():"],
            ai_answer=["def my_func():"],
            user_answer=["function my_func():"],  # Mistake: incorrect syntax
            evaluation="The correct answer is 'def my_func():'",
            score=0
        },
        {
            question_type="multiple_choice",
            question="What are the valid data types in Python?",
            options=["int", "string", "boolean", "number"],
            ai_answer=["int", "string", "boolean"],
            user_answer=["int", "number"],  # Mistake: 'number' is not a valid data type in Python
            evaluation="The answer is partially correct. 'number' is not a valid data type in Python. The correct types are 'int', 'string', and 'boolean'.",
            score=3
        }]
}
-----
{{submission}}
"""

SUBMISSION_FORMATTER="""Format input to exam submission json object format :
Exam Submission Json Object:
{
  "exam": [
    {
      "question_type": "single_choice"/"multiple_choice"/"essay",
      "question": "string",
      "options": [
        "string"
      ],
      "ai_answer": [
        "string"
      ],
      "user_answer": [
       "string"
      ],
      "evaluation": "string",
      "score": int
    },
    "feedback": "string"}
--------------------------------
{{input}}"""