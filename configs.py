# configs.py

import os

# Model configurations
MODEL_NAME = "llama3.2"
REQUEST_TIMEOUT = 120.0

# Embedding model configurations
EMBEDDING_MODEL_NAME = "BAAI/bge-large-en-v1.5"
TRUST_REMOTE_CODE = True

# Data loader configurations
INPUT_DIRS = [  # List of directories where your documents are stored
    "documents",  # First directory
    "/mnt/d/Paper",
    # Add more directories as needed
]
REQUIRED_EXTS = [".pdf", ".doc"]  # File extensions to be considered for indexing
RECURSIVE = True  # Whether to load files recursively from subdirectories

# Index persistence directory
PERSIST_DIR = "storage"  # Directory to store the index files (e.g., 'storage/')

# ChromaDB configurations
CHROMA_DB_DIR = "chroma_db"  # Directory to store ChromaDB data
CHROMA_COLLECTION_NAME = "my_collection"  # Name of the ChromaDB collection

# Indexed files metadata path
INDEXED_FILES_PATH = "indexed_files.json"  # Path to store indexed files metadata

# Default query
QUERY = "For lotus framework, do we need to convert the table into pandas first?"

# Create directories if they don't exist
os.makedirs(PERSIST_DIR, exist_ok=True)  # Create storage directory if it doesn't exist
os.makedirs(
    CHROMA_DB_DIR, exist_ok=True
)  # Create ChromaDB directory if it doesn't exist
