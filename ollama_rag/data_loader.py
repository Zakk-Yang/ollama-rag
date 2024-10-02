# data_loader.py

from llama_index.core import SimpleDirectoryReader
import os
from typing import List
import logging
from llama_index.core import Document
import subprocess
import shutil
from llama_index.core.readers.base import BaseReader
from llama_index.readers.file.slides.base import PptxReader
from llama_index.readers.file.tabular.base import (
    CSVReader,
)
from ollama_rag.configs import REQUIRED_EXTS
import logging
import pandas as pd

# Configure logging for this module
logger = logging.getLogger(__name__)


# Custom PPT Reader to handle PPT files by converting them to PPTX
class PPTReader(BaseReader):
    def load_data(self, file: str, extra_info=None):
        # Check if 'libreoffice' is available
        if not shutil.which("libreoffice"):
            logging.error("'libreoffice' is not installed or not found in PATH.")
            return []

        try:
            output_dir = os.path.dirname(file)
            subprocess.run(
                [
                    "libreoffice",
                    "--headless",
                    "--convert-to",
                    "pptx",
                    "--outdir",
                    output_dir,
                    file,
                ],
                check=True,
            )
            converted_file_path = os.path.splitext(file)[0] + ".pptx"
            if os.path.exists(converted_file_path):
                logging.info(f"Converted {file} to {converted_file_path}")
                # Now use the built-in PptxReader
                pptx_reader = PptxReader()
                return pptx_reader.load_data(converted_file_path, extra_info=extra_info)
            else:
                logging.error(f"Conversion failed for {file}")
                return []
        except Exception as e:
            logging.error(f"Error converting {file} to PPTX: {e}")
            return []


class CustomExcelReader(BaseReader):
    def load_data(self, file: str, extra_info=None) -> List[Document]:
        """
        Read an Excel file and return documents, including sheet_name in metadata.

        Parameters:
        - file (str): Path to the Excel file.
        - extra_info (dict, optional): Additional metadata.

        Returns:
        - List[Document]: Documents created from the Excel file.
        """
        if extra_info is None:
            extra_info = {}

        try:
            # Read the Excel file
            excel_file = pd.ExcelFile(file)
            documents = []

            for sheet_name in excel_file.sheet_names:
                # Read each sheet into a DataFrame
                df = pd.read_excel(excel_file, sheet_name=sheet_name)

                # Convert DataFrame to CSV format (or any preferred text format)
                text = df.to_csv(index=False)

                # Create metadata including sheet_name
                metadata = {
                    "file_name": os.path.basename(file),
                    "file_path": os.path.abspath(file),
                    "sheet_name": sheet_name,
                }
                # Merge with extra_info if provided
                metadata.update(extra_info)

                # Create Document with text and metadata
                doc = Document(text=text, metadata=metadata)
                documents.append(doc)

            return documents

        except Exception as e:
            logger.error(f"Error reading Excel file {file}: {e}")
            return []


def load_data(
    input_dirs: List[str], required_exts: List[str] = None, recursive: bool = True
) -> List[Document]:
    """
    Load data from the specified list of input directories with detailed metadata using SimpleDirectoryReader.

    Parameters:
    - input_dirs (List[str]): A list of directory paths to load files from.
    - required_exts (List[str], optional): A list of file extensions to include. Defaults to common extensions.
    - recursive (bool, optional): Whether to include files from subdirectories. Defaults to True.

    Returns:
    - List[Document]: A list of Document objects containing text and metadata.
    """
    if required_exts is None:
        # Default to common file extensions
        required_exts = REQUIRED_EXTS

    # Define custom file extractors for unsupported or special file types
    file_extractor = {
        ".ppt": PPTReader(),  # Custom reader for .ppt files
        ".xls": CustomExcelReader(),  # Built-in reader for .xls files
        ".xlsx": CustomExcelReader(),  # Built-in reader for .xlsx files
        ".csv": CSVReader(),  # Built-in reader for .csv files
        # Add other custom readers here if needed
    }

    all_documents = []

    for input_dir in input_dirs:
        if not os.path.isdir(input_dir):
            logger.warning(
                f"Input directory '{input_dir}' does not exist or is not a directory. Skipping..."
            )
            continue

        logger.info(f"Processing directory: {input_dir}")

        # Initialize SimpleDirectoryReader within try-except to catch initialization errors
        try:
            reader = SimpleDirectoryReader(
                input_dir=input_dir,
                recursive=recursive,
                file_extractor=file_extractor,
                required_exts=required_exts,
            )

            documents = reader.load_data()
            if not documents:
                logger.warning(f"No documents found in '{input_dir}'. Skipping...")
                continue
            all_documents.extend(documents)
            logger.info(f"Loaded {len(documents)} documents from '{input_dir}'")
        except ValueError as ve:
            logger.warning(f"{ve} Skipping '{input_dir}'.")
        except Exception as e:
            logger.error(f"Failed to load data from '{input_dir}': {e}")

    return all_documents


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
