from haystack import Pipeline
from haystack.components.converters import AzureOCRDocumentConverter
from haystack.components.preprocessors import DocumentCleaner
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.writers import DocumentWriter
from haystack.utils import Secret
from haystack import component
from haystack.components.builders import PromptBuilder
from haystack.components.generators import AzureOpenAIGenerator
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore


from haystack import component
from haystack import Document
import os
from dotenv import load_dotenv
from haystack.components.embedders import AzureOpenAIDocumentEmbedder
load_dotenv()
@component
class SummaryKeywordPipeLine:
  """
  A component extract document summary and keywords
  """
  def __init__(self):
    self.pipeline = Pipeline()
    summary_client = AzureOpenAIGenerator(azure_endpoint=os.getenv("AZURE_ENDPOINT"),
                        api_key=Secret.from_token(os.getenv("AZURE_OPENAI_KEY")),
                        azure_deployment=os.getenv("CHAT_COMPLETIONS_MODEL"))
    summary_template = "Give me main points of my documents. Documents:\n  {{ document }}"
    keyword_client = AzureOpenAIGenerator(azure_endpoint=os.getenv("AZURE_ENDPOINT"),
                        api_key=Secret.from_token(os.getenv("AZURE_OPENAI_KEY")),
                        azure_deployment=os.getenv("CHAT_COMPLETIONS_MODEL"))
    keyword_template = "Give me list of keywords of my documents. Example: \n{{example_extract_keywords}}\nResult:{{keywords_sample}}} Documents:\n  {{ document }}\nResults:"
    summary_builder = PromptBuilder(template=summary_template)
    keyword_builder = PromptBuilder(template=keyword_template)
    self.pipeline.add_component("summary_builder", summary_builder)
    self.pipeline.add_component("summary_generator", summary_client)
    self.pipeline.add_component("keyword_builder", keyword_builder)
    self.pipeline.add_component("keyword_generator", keyword_client)
    self.pipeline.connect("summary_builder", "summary_generator")
    self.pipeline.connect("keyword_builder", "keyword_generator")
    
  @component.output_types(documents=list[Document])
  def run(self,documents:list[Document]):
    example_extract_keywords = """Documents:
    Cloud computing allows users to access computing resources over the internet. It provides scalable and flexible computing services, such as storage, networking, and databases. There are several types of cloud computing: public, private, and hybrid. With cloud computing, users can deploy applications, store data, and perform computing tasks without owning or maintaining the physical infrastructure."""
    keywords_sample = ["cloud computing", "scalability", "flexibility", "public cloud", "private cloud", "hybrid cloud", "internet resources"]
    for doc in documents:
      results=self.pipeline.run({"summary_builder": {"document": doc.content},"keyword_builder": {"document": doc.content,"example_extract_keywords": example_extract_keywords,"keywords_sample": keywords_sample}},include_outputs_from=["summary_generator","keyword_generator"])
      doc.meta={"summary":results["summary_generator"]["replies"][0],"keywords":results["keyword_generator"]["replies"][0]}
    return {"documents":documents}
  
@component
class DocumentPipeline(Pipeline):
    def __init__(self):
        super().__init__()
        self.document_store = QdrantDocumentStore(
        url=os.getenv("QDRANT_API_URL"),api_key=Secret.from_env_var("QDRANT_API_KEY"),embedding_dim=1536,index=os.getenv("QDRANT_INDEX")
        )
        self.embeder=AzureOpenAIDocumentEmbedder(azure_endpoint=os.getenv("AZURE_ENDPOINT"),
                        api_key=Secret.from_token(os.getenv("AZURE_OPENAI_KEY")),
                        azure_deployment=os.getenv("EMBEDDING_MODEL"),meta_fields_to_embed=["summary","keywords"])
        self.add_component("converter", AzureOCRDocumentConverter(endpoint=os.environ["AZURE_DOC_ENDPOINT"], api_key=Secret.from_token(os.environ["AZURE_DOC_KEY"])))
        self.add_component("cleaner", DocumentCleaner())
        self.add_component("splitter", DocumentSplitter(split_by="passage", split_length=5))
        self.add_component("summary_keyword", SummaryKeywordPipeLine())
        self.add_component("embeder", self.embeder)
        self.add_component("writer", DocumentWriter(document_store=self.document_store))
        self.connect("converter", "cleaner")
        self.connect("cleaner", "splitter")
        self.connect("splitter", "summary_keyword")
        self.connect("summary_keyword", "embeder")
        self.connect("embeder", "writer")

# Example usage
if __name__ == "__main__":
  file_names = ["Question Answering and Quiz Generation Chatbot for Education.pdf"]

  document_pipeline = DocumentPipeline()
  result=document_pipeline.run({"converter": {"sources": file_names}})
  # print(result["summary_keyword"]["documents"][0].meta)