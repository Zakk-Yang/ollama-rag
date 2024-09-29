# models.py

from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from ollama_rag.configs import MODEL_NAME, REQUEST_TIMEOUT, EMBEDDING_MODEL_NAME, TRUST_REMOTE_CODE

def setup_llm(model_name=MODEL_NAME, request_timeout=REQUEST_TIMEOUT):
    """Set up the LLM model."""
    try:
        llm = Ollama(model=model_name, request_timeout=request_timeout)
        return llm
    except Exception as e:
        raise Exception(f"Failed to set up LLM: {e}")

def setup_embedding_model(model_name=EMBEDDING_MODEL_NAME, trust_remote_code=TRUST_REMOTE_CODE):
    """Set up the embedding model."""
    try:
        embed_model = HuggingFaceEmbedding(model_name=model_name, trust_remote_code=trust_remote_code)
        return embed_model
    except Exception as e:
        raise Exception(f"Failed to set up embedding model: {e}")
