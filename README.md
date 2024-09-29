# Llama Index Query Engine Project

This project is a robust and modular application that builds an efficient query engine using LlamaIndex, ChromaDB, and custom embeddings. It allows you to index documents from multiple directories and query them using natural language.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Adding Documents](#adding-documents)
- [Logging](#logging)
- [Handling Missing Index Files](#handling-missing-index-files)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Modular Design**: The project is organized into separate modules for easy maintenance and scalability.
- **Efficient Indexing**: Uses ChromaDB to store embeddings, allowing efficient indexing and querying.
- **Incremental Updates**: Only new or updated documents are indexed, improving performance.
- **Multiple Directories Support**: Indexes documents from multiple directories across different locations.
- **Custom Embeddings**: Utilizes custom embedding models for better performance.
- **Error Handling**: Gracefully handles missing directories or files and recreates the index as needed.
- **Logging**: Provides detailed logs for monitoring and debugging.

## Project Structure
my_llama_project/ ├── main.py ├── models.py ├── data_loader.py ├── indexer.py ├── query_engine.py ├── prompts.py ├── configs.py ├── document_tracker.py ├── requirements.txt ├── storage/ # Generated index data (ignored by Git) ├── chroma_db/ # ChromaDB data (ignored by Git) ├── indexed_files.json # Indexed files metadata (ignored by Git) └── documents/ # User documents (ignored by Git)
