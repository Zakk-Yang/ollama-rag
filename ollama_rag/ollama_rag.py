# ollama_rag.py

import logging
from llama_index.core import Settings
from ollama_rag.models import setup_llm, setup_embedding_model
from ollama_rag.data_loader import load_data
from ollama_rag.indexer import create_index, load_index
from ollama_rag.query_engine import create_query_engine
from ollama_rag.prompts import qa_prompt_template
from ollama_rag.document_tracker import (
    load_indexed_files,
    save_indexed_files,
    get_new_or_updated_files,
    update_indexed_files,
)
import os
import argparse
from ollama_rag.configs import (
    MODEL_NAME,
    EMBEDDING_MODEL_NAME,
    PERSIST_DIR,
    CHROMA_DB_DIR,
    CHROMA_COLLECTION_NAME,
    INDEXED_FILES_PATH,
    REQUIRED_EXTS,
)


class OllamaRAG:
    def __init__(
        self,
        model_name=MODEL_NAME,
        request_timeout=120.0,
        embedding_model_name=EMBEDDING_MODEL_NAME,
        trust_remote_code=True,
        input_dirs=None,
        required_exts=REQUIRED_EXTS,
        recursive=True,
        persist_dir=PERSIST_DIR,
        chroma_db_dir=CHROMA_DB_DIR,
        chroma_collection_name=CHROMA_COLLECTION_NAME,
        indexed_files_path=INDEXED_FILES_PATH,
        query=None,
        qa_prompt_template=qa_prompt_template,
    ):
        if input_dirs is None:
            input_dirs = []
        if required_exts is None:
            required_exts = []

        # Store parameters as instance variables
        self.model_name = model_name
        self.request_timeout = request_timeout
        self.embedding_model_name = embedding_model_name
        self.trust_remote_code = trust_remote_code
        self.input_dirs = input_dirs
        self.required_exts = required_exts
        self.recursive = recursive
        self.persist_dir = persist_dir
        self.chroma_db_dir = chroma_db_dir
        self.chroma_collection_name = chroma_collection_name
        self.indexed_files_path = indexed_files_path
        self.query_text = query
        self.qa_prompt_template = qa_prompt_template

        # Create directories if they don't exist
        os.makedirs(self.persist_dir, exist_ok=True)
        os.makedirs(self.chroma_db_dir, exist_ok=True)

        # Setup logging
        logging.basicConfig(level=logging.INFO)

        try:
            # Setup LLM and embedding model
            logging.info("Setting up LLM and embedding model...")
            self.llm = setup_llm(
                model_name=self.model_name, request_timeout=self.request_timeout
            )
            self.embed_model = setup_embedding_model(
                model_name=self.embedding_model_name,
                trust_remote_code=self.trust_remote_code,
            )

            # Set global settings
            Settings.llm = self.llm
            Settings.embed_model = self.embed_model

            # Load index if it exists
            logging.info("Checking for existing index...")
            self.index = load_index(
                persist_dir=self.persist_dir,
                chroma_db_dir=self.chroma_db_dir,
                chroma_collection_name=self.chroma_collection_name,
            )

            # Load indexed files metadata
            self.indexed_files = load_indexed_files(
                indexed_files_path=self.indexed_files_path
            )

        except Exception as e:
            logging.error(f"An error occurred during initialization: {e}")
            raise

    def update_index(self):
        """Update the index with new or updated files."""
        new_or_updated_files = get_new_or_updated_files(
            self.input_dirs,
            self.required_exts,
            self.recursive,
            self.indexed_files,
        )

        if new_or_updated_files:
            # Log new or updated files
            logging.info("New or updated files detected:")
            for file in new_or_updated_files:
                logging.info(f"- {file}")

            # Load data from new or updated files
            docs = load_data(files=new_or_updated_files)
            if not docs:
                logging.error("No new documents to index.")
                return

            if self.index is None:
                # Create index with new documents
                logging.info("Creating a new index with new documents...")
                self.index = create_index(
                    docs,
                    persist_dir=self.persist_dir,
                    chroma_db_dir=self.chroma_db_dir,
                    chroma_collection_name=self.chroma_collection_name,
                )
            else:
                # Insert new documents into the existing index
                logging.info("Inserting new documents into the existing index...")
                for doc in docs:
                    self.index.insert(doc)
                # Persist the updated index
                self.index.storage_context.persist(persist_dir=self.persist_dir)

            # Update indexed files metadata
            update_indexed_files(self.indexed_files, new_or_updated_files)
            save_indexed_files(
                self.indexed_files, indexed_files_path=self.indexed_files_path
            )
        else:
            if self.index is None:
                logging.error("No existing index and no new documents to index.")
                return
            else:
                logging.info("No new or updated documents found.")

        # Create query engine
        logging.info("Setting up query engine...")
        self.query_engine = create_query_engine(self.index, self.qa_prompt_template)

    def query(self, query_text=None):
        """Run a query against the index."""
        if query_text is None:
            query_text = self.query_text

        if not hasattr(self, "query_engine"):
            logging.error(
                "Query engine not initialized. Please run update_index() first."
            )
            return

        # Generate the response
        logging.info(f"Running query: {query_text}")
        response = self.query_engine.query(query_text)
        print(response)
        return response


# def main():
#     parser = argparse.ArgumentParser(description="Run the Ollama RAG query engine.")
#     parser.add_argument(
#         "--query",
#         type=str,
#         required=True,
#         help="The query to run against the index.",
#     )
#     parser.add_argument(
#         "--input_dirs",
#         type=str,
#         nargs="+",
#         default=["/mnt/d/Paper"],
#         help="""Directories containing documents to index. Example: ollama-rag --query "Your custom query here" --input_dirs /path/to/your/documentfolder1 /path/to/your/documentfolder2""",
#     )
#     parser.add_argument(
#         "--required_exts",
#         type=str,
#         nargs="+",
#         default=[
#             ".txt",
#             ".md",
#             ".html",
#             ".htm",
#             ".xml",
#             ".json",
#             ".csv",
#             ".pdf",
#             ".doc",
#             ".docx",
#             ".rtf",
#             ".ipynb",
#         ],
#         help="List of file extensions to include for indexing.",
#     )

#     args = parser.parse_args()
#     MODEL_NAME,
#     EMBEDDING_MODEL_NAME,
#     PERSIST_DIR,
#     CHROMA_DB_DIR,
#     CHROMA_COLLECTION_NAME,
#     INDEXED_FILES_PATH,
#     REQUIRED_EXTS,
#     # Initialize the OllamaRAG engine with provided configurations
#     engine = OllamaRAG(
#         model_name= MODEL_NAME,
#         request_timeout=120.0,
#         embedding_model_name="BAAI/bge-large-en-v1.5",
#         trust_remote_code=True,
#         input_dirs=args.input_dirs,
#         required_exts=args.required_exts,
#         recursive=True,
#         persist_dir=args.persist_dir,
#         chroma_db_dir=args.chroma_db_dir,
#         chroma_collection_name=args.chroma_collection_name,
#         indexed_files_path=args.indexed_files_path,
#         query=args.query,
#     )

#     # Update the index with new or updated documents
#     engine.update_index()

#     # Run the query
#     engine.query()


# if __name__ == "__main__":
#     main()
