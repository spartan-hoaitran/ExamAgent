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
