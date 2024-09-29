# data_loader.py

from llama_index.core import SimpleDirectoryReader
import os


def load_data(files):
    """Load data from the specified list of files."""
    if not files:
        return []
    try:
        loader = SimpleDirectoryReader(input_files=files)
        docs = loader.load_data()
        return docs
    except Exception as e:
        raise Exception(f"Failed to load data: {e}")


def get_all_files(input_dirs, required_exts, recursive):
    """Get all files from the list of input directories."""
    all_files = []
    for input_dir in input_dirs:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if any(file.lower().endswith(ext) for ext in required_exts):
                    file_path = os.path.join(root, file)
                    all_files.append(file_path)
            if not recursive:
                break
    return all_files
