from haystack import Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.converters import AzureOCRDocumentConverter
from haystack.components.preprocessors import DocumentCleaner
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.writers import DocumentWriter
from haystack.utils import Secret

document_store = InMemoryDocumentStore()

pipeline = Pipeline()
pipeline.add_component("converter", AzureOCRDocumentConverter(endpoint="azure_resource_url", api_key=Secret.from_token("<your-api-key>")))
pipeline.add_component("cleaner", DocumentCleaner())
pipeline.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=5))
pipeline.add_component("writer", DocumentWriter(document_store=document_store))
pipeline.connect("converter", "cleaner")
pipeline.connect("cleaner", "splitter")
pipeline.connect("splitter", "writer")

file_names = ["my_file.pdf"]
pipeline.run({"converter": {"sources": file_names}})