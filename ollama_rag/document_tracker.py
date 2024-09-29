# document_tracker.py

import os
import json
from ollama_rag.configs import INDEXED_FILES_PATH


def load_indexed_files(indexed_files_path):
    """Load indexed files metadata from disk."""
    if os.path.exists(indexed_files_path):
        with open(indexed_files_path, "r") as f:
            return json.load(f)
    else:
        return {}


def save_indexed_files(indexed_files, indexed_files_path):
    """Save indexed files metadata to disk."""
    with open(indexed_files_path, "w") as f:
        json.dump(indexed_files, f)


def get_new_or_updated_files(input_dirs, required_exts, recursive, indexed_files):
    """Get a list of new or updated files to index from multiple directories."""
    new_or_updated_files = []
    for input_dir in input_dirs:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if any(file.lower().endswith(ext) for ext in required_exts):
                    file_path = os.path.join(root, file)
                    mtime = os.path.getmtime(file_path)
                    stored_mtime = indexed_files.get(file_path)
                    if stored_mtime is None or mtime > stored_mtime:
                        new_or_updated_files.append(file_path)
            if not recursive:
                break
    return new_or_updated_files


def update_indexed_files(indexed_files, files):
    """Update indexed files metadata with new modification times."""
    for file_path in files:
        mtime = os.path.getmtime(file_path)
        indexed_files[file_path] = mtime
