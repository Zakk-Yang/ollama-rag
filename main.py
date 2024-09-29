# main.py

import os
import logging
import argparse
from dotenv import load_dotenv

from models import setup_llm, setup_embedding_model
from data_loader import load_data
from indexer import create_index, load_index
from query_engine import create_query_engine
from prompts import qa_prompt_template
from configs import QUERY
from llama_index.core import Settings  # Import Settings
from configs import QUERY, PERSIST_DIR, INPUT_DIRS, REQUIRED_EXTS, RECURSIVE
from document_tracker import (
    load_indexed_files,
    save_indexed_files,
    get_new_or_updated_files,
    update_indexed_files,
)
from configs import (
    QUERY,
    PERSIST_DIR,
    INPUT_DIRS,
    REQUIRED_EXTS,
    RECURSIVE,
)


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run the LLM query engine.")
    parser.add_argument(
        "--query", type=str, default=QUERY, help="The query to run against the index."
    )
    args = parser.parse_args()
    query = args.query

    # Load environment variables
    load_dotenv()

    # Setup logging
    logging.basicConfig(level=logging.INFO)

    try:
        # Setup LLM and embedding model
        logging.info("Setting up LLM and embedding model...")
        llm = setup_llm()
        embed_model = setup_embedding_model()

        # Set global settings
        Settings.llm = llm
        Settings.embed_model = embed_model

        # Load index if it exists, otherwise recreate it
        logging.info("Checking for existing index...")
        index = load_index()

        # Load indexed files metadata
        indexed_files = load_indexed_files()

        # Get new or updated files
        new_or_updated_files = get_new_or_updated_files(
            INPUT_DIRS, REQUIRED_EXTS, RECURSIVE, indexed_files
        )

        if new_or_updated_files:
            # Log new or updated files
            logging.info("New or updated files detected:")
            for file in new_or_updated_files:
                logging.info(f"- {file}")

            # Load data from new or updated files
            docs = load_data(files=new_or_updated_files)
            if not docs:
                logging.error("No new documents to index. Exiting...")
                return

            if index is None:
                # Create index with new documents
                logging.info("Creating a new index with new documents...")
                index = create_index(docs)
            else:
                # Insert new documents into the existing index
                logging.info("Inserting new documents into the existing index...")
                for doc in docs:
                    index.insert(doc)
                # Persist the updated index
                index.storage_context.persist(persist_dir=PERSIST_DIR)

            # Update indexed files metadata
            update_indexed_files(indexed_files, new_or_updated_files)
            save_indexed_files(indexed_files)
        else:
            if index is None:
                logging.error(
                    "No existing index and no new documents to index. Exiting..."
                )
                return
            else:
                logging.info("No new or updated documents found.")

        # Create query engine
        logging.info("Setting up query engine...")
        query_engine = create_query_engine(index, qa_prompt_template)

        # Generate the response
        logging.info(f"Running query: {query}")
        response = query_engine.query(query)

        print("\nResponse:")
        print(response)

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
