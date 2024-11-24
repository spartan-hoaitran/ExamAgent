from haystack import Pipeline
from haystack.utils import Secret
import os
from dotenv import load_dotenv
from haystack.components.embedders import AzureOpenAITextEmbedder
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
from haystack_integrations.components.retrievers.qdrant import QdrantEmbeddingRetriever
from haystack import Pipeline
from haystack.components.builders import PromptBuilder
from dotenv import load_dotenv
from haystack.components.generators import AzureOpenAIGenerator
import re
import json
from schemas.exam_schemas import InputCreateExam
from .prompt import CREATE_QUESTION_GPT, QUESTION_FORMATTER
load_dotenv()
def json_object_formatter(input_string):
        """
        Extracts the JSON block that starts with ```json and ends with ```.

        Args:
            input_string (str): The input string containing the JSON block.

        Returns:
            str: The extracted JSON block, or an error message if no block is found.
        """
        # Use regex to capture everything between ```json and ```
        match = re.search(r'```json(.*?)```', input_string, re.DOTALL)
        try:
            if match:
                # Extract and return the content, stripped of leading/trailing spaces
                result=json.loads(match.group(1).strip())
                for question in result:
                    if "question" not in question:
                        result.remove(question)
                return result
            else:
                # Inform the user if no match is found
                return None
        except Exception as e:
            return None
class CreateQuestionPipeline():
    def __init__(self):
        pass

    
    def find_similar_documents(self,description:str):
        print("-----------------")
        pipeline=Pipeline()
        document_store = QdrantDocumentStore(
        url=os.getenv("QDRANT_API_URL"),api_key=Secret.from_env_var("QDRANT_API_KEY"),embedding_dim=1536,index=os.getenv("QDRANT_INDEX")
        )
        embedder=AzureOpenAITextEmbedder(azure_endpoint=os.getenv("AZURE_ENDPOINT"),
                        api_key=Secret.from_token(os.getenv("AZURE_OPENAI_KEY")),
                        azure_deployment=os.getenv("EMBEDDING_MODEL"))
        pipeline.add_component("embedder",embedder)
        pipeline.add_component("retriever", QdrantEmbeddingRetriever(document_store=document_store))
        pipeline.connect("embedder.embedding", "retriever.query_embedding")
        results = pipeline.run({"embedder": {"text": description}})
        return results["retriever"]["documents"]
    
    def create_question(self,exam:InputCreateExam):
        docs=self.find_similar_documents(exam.description)
        total_questions_single=int(exam.total_question*exam.ratio_question["single_choice"])
        total_questions_multiple=int(exam.total_question*exam.ratio_question["multiple_choice"])
        total_questions_essay=int(exam.total_question*exam.ratio_question["essay"])
        single_choice_questions=[]
        multiple_choice_questions=[]
        essay_questions=[]
        # while exam.total_question>(len(single_choice_questions)+len(multiple_choice_questions)+len(essay_questions)):
        for doc in docs:
            question=self.create_question_by_gpt(doc,exam.description,question_type="single_choice",number_of_questions=int(total_questions_single/len(docs)))
            if question:
                single_choice_questions.extend(question)
            question=self.create_question_by_gpt(doc,exam.description,question_type="multiple_choice",number_of_questions=int(total_questions_multiple/len(docs)))
            if question:
                multiple_choice_questions.extend(question)
            question=self.create_question_by_gpt(doc,exam.description,question_type="essay",number_of_questions=int(total_questions_essay/len(docs)))
            if question:
                essay_questions.extend(question)
        
        return single_choice_questions[:total_questions_single],multiple_choice_questions[:total_questions_multiple],essay_questions[:total_questions_essay]
        
    def create_question_by_gpt(self,document,description_of_exam:str,question_type,number_of_questions:int):
        pipeline=Pipeline()
        client = AzureOpenAIGenerator(azure_endpoint=os.getenv("AZURE_ENDPOINT"),
                        api_key=Secret.from_token(os.getenv("AZURE_OPENAI_KEY")),
                        azure_deployment=os.getenv("CHAT_COMPLETIONS_MODEL"))
        formatter_client = AzureOpenAIGenerator(azure_endpoint=os.getenv("AZURE_ENDPOINT"),
                        api_key=Secret.from_token(os.getenv("AZURE_OPENAI_KEY")),
                        azure_deployment=os.getenv("CHAT_COMPLETIONS_MODEL"))
        prompt_builder = PromptBuilder(template=CREATE_QUESTION_GPT)
        formatter_prompt_builder = PromptBuilder(template=QUESTION_FORMATTER)
        pipeline.add_component("prompt_builder", prompt_builder)
        pipeline.add_component("generator", client)
        pipeline.add_component("formatter_prompt_builder", formatter_prompt_builder)
        pipeline.add_component("formatter_generator", formatter_client)
        pipeline.connect("prompt_builder", "generator")
        pipeline.connect("generator.replies", "formatter_prompt_builder")
        pipeline.connect("formatter_prompt_builder", "formatter_generator")
        results=pipeline.run({"prompt_builder": {"question_type":question_type,"number_of_questions":number_of_questions,
                        "rule":description_of_exam,
                        "document":document}})
        results=json_object_formatter(results["formatter_generator"]["replies"][0])
        return results
    


