# indexer.py

from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
import os
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
import logging

INDEX_SAVE_PATH = "index.json"  # Path to save the index


def load_index(persist_dir, chroma_db_dir, chroma_collection_name):
    """Load the index from disk if it exists and is complete."""
    if os.path.exists(persist_dir):
        try:
            # Initialize Chroma client and collection
            chroma_client = chromadb.PersistentClient(path=chroma_db_dir)
            chroma_collection = chroma_client.get_or_create_collection(
                chroma_collection_name
            )
            vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
            # Specify persist_dir when loading existing index
            storage_context = StorageContext.from_defaults(
                persist_dir=persist_dir, vector_store=vector_store
            )

            # Attempt to load the index from storage
            index = load_index_from_storage(storage_context)
            return index
        except FileNotFoundError as e:
            # Log an error and indicate that the index cannot be loaded due to missing files
            logging.error(f"Index file not found: {e}")
            logging.info(
                "The storage directory or some index files are missing. A new index will be created."
            )
            return None
        except Exception as e:
            # Handle other errors that may occur while loading the index
            logging.error(f"Failed to load index due to an unexpected error: {e}")
            return None
    else:
        # If the storage directory itself doesn't exist, return None to indicate the absence of an index
        logging.info(
            "The storage directory does not exist. A new index will be created."
        )
        return None


def create_index(docs, persist_dir, chroma_db_dir, chroma_collection_name):
    """Create an index from the documents."""
    if not docs:
        raise ValueError("No documents provided for indexing.")
    try:
        # Initialize Chroma client and collection
        chroma_client = chromadb.PersistentClient(path=chroma_db_dir)
        chroma_collection = chroma_client.get_or_create_collection(
            chroma_collection_name
        )
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # Create the index with the storage context
        index = VectorStoreIndex.from_documents(
            docs,
            storage_context=storage_context,
            show_progress=True,
        )

        # Persist the index
        index.storage_context.persist(persist_dir=persist_dir)
        return index
    except Exception as e:
        logging.error(f"Failed to create index: {e}")
        raise
