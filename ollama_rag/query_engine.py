# query_engine.py

from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader


def create_query_engine(index, qa_prompt_template=None):
    """Set up the query engine."""
    try:
        query_engine = index.as_query_engine(text_qa_template=qa_prompt_template)
        return query_engine
    except Exception as e:
        raise Exception(f"Failed to create query engine: {e}")
