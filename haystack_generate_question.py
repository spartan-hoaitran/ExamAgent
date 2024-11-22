from haystack import Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.converters import AzureOCRDocumentConverter
from haystack.components.preprocessors import DocumentCleaner
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.writers import DocumentWriter
from haystack.utils import Secret
from haystack import component
from haystack.components.builders import PromptBuilder
from haystack.components.generators import AzureOpenAIGenerator
from haystack_integrations.document_stores.elasticsearch import ElasticsearchDocumentStore
from haystack import component
from haystack import Document
@component
class SummarizerÁndKeywordExtractorResultFormatter:
  """
  A component generating personal welcome message and making it upper case
  """
  @component.output_types(docs=list[Document])
  def run(self,docs=list[Document]):
    pipeline = Pipeline()
    client = AzureOpenAIGenerator(azure_endpoint="<Your Azure endpoint e.g. `https://your-company.azure.openai.com/>",
                        api_key=Secret.from_token("<your-api-key>"),
                        azure_deployment="<a model name>")
    template = "Summary and give me some keywords of my documents. Context:\n  {{ document }}"
    builder = PromptBuilder(template=template)
    pipeline.add_component("builder", builder)
    pipeline.add_component("generator", client)
    for doc in docs:
        doc.meta["summary"] = doc.meta["summary"].upper()
        doc.meta["keywords"] = doc.meta["keywords"].upper()
    return {"welcome_text": f'Hello {name}, welcome to Haystack!'.upper(), "note": "welcome message is ready"}

class DocumentPipeline(Pipeline):
    def __init__(self, azure_endpoint, azure_api_key):
        super().__init__()
        document_store = ElasticsearchDocumentStore()
        client = AzureOpenAIGenerator(azure_endpoint="<Your Azure endpoint e.g. `https://your-company.azure.openai.com/>",
                        api_key=Secret.from_token("<your-api-key>"),
                        azure_deployment="<a model name>")
        template = "Summary and give me some keywords of my documents. Context:\n  {{ document }}"
        builder = PromptBuilder(template=template)
        self.add_component("converter", AzureOCRDocumentConverter(endpoint=azure_endpoint, api_key=Secret.from_token(azure_api_key)))
        self.add_component("cleaner", DocumentCleaner())
        self.add_component("splitter", DocumentSplitter(split_by="passage", split_length=5))
        self.add_component("writer", DocumentWriter(document_store=self.document_store))
        self.connect("converter", "cleaner")
        self.connect("cleaner", "splitter")
        self.connect("splitter", "writer")

    def run_pipeline(self, file_names):
        self.run({"converter": {"sources": file_names}})

# Example usage
azure_endpoint = "azure_resource_url"
azure_api_key = "<your-api-key>"
file_names = ["my_file.pdf"]

document_pipeline = DocumentPipeline(azure_endpoint, azure_api_key)
document_pipeline.run_pipeline(file_names)