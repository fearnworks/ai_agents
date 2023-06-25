from langchain.embeddings.openai import OpenAIEmbeddings
from dataclasses import dataclass
import os 

@dataclass
class OpenAIEmbedConfig:
    openai_api_key: str

def get_default_openai_embeddings() -> OpenAIEmbeddings:
    """
    Returns a default OpenAIEmbeddings instance with a default API key.

    Returns:
        OpenAIEmbeddings: A new OpenAIEmbeddings instance.
    """
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    return embeddings