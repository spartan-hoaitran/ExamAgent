import os
from haystack import Pipeline, Document
from haystack.components.generators import AzureOpenAIGenerator
from haystack.components.builders.prompt_builder import PromptBuilder
# Imports needed to run this notebook
from haystack.utils import Secret
from haystack.components.preprocessors import DocumentCleaner

from haystack.components.converters import AzureOCRDocumentConverter
from haystack.utils import Secret


class DocumentPipeline(Pipeline):
    def __init__(self, azure_endpoint, api_version, api_key, azure_deployment):
        super().__init__()
        doc_converter = AzureOCRDocumentConverter(
                            endpoint="azure_resource_url",
                            api_key=Secret.from_token("<your-api-key>")
                        )
        doc_cleaner = DocumentCleaner(ascii_only=True,
                                remove_empty_lines=True,
                                remove_extra_whitespaces=True,
                                remove_repeated_substrings=False)
        

