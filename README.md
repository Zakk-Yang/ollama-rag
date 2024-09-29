# Llama Index Query Engine + Ollama Model to Create Your Own Knowledge Pool

This project is a robust and modular application that builds an efficient query engine using LlamaIndex, ChromaDB, and custom embeddings. It allows you to index documents from multiple directories and query them using natural language.

Input Question Example: where can i find the adress of Jason Black?
Output example: The address is 'xxx, xxx, xxx'



## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
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
- **Advanced Text-Based File Support**: Supports a variety of text-based file formats, including:
  - **Text Files**: Plain text (.txt), Markdown (.md), HTML (.html, .htm), XML (.xml), CSV (.csv).
  - **Document Files**: PDF (.pdf), Microsoft Word (.doc, .docx), Rich Text Format (.rtf).
  - **Jupyter Notebooks**: Jupyter Notebook (.ipynb).

## Project Structure
```graphql
ollama_rag/
├── ollama_rag/
│   ├── __init__.py
│   ├── ollama_rag.py         # Main class OllamaRAG
│   ├── models.py
│   ├── data_loader.py
│   ├── indexer.py
│   ├── query_engine.py
│   ├── prompts.py
│   ├── document_tracker.py
│ 
├── tests/
│   └── ... (test scripts)
├── setup.py
├── README.md
├── LICENSE
├── MANIFEST.in
└── requirements.txt
```

## Prerequisites

- **Python 3.7 or higher**: Ensure you have Python installed.
- **Git**: For cloning the repository.
- **Pip**: Python package installer.

## Installation
### Install via PyPI (Recommended)
You can install `ollama_rag` directly from PyPI:
```bash
pip install --upgrade ollama-rag
```

### Install from Source
1. **Clone the Repository**

   ```bash
   git clone https://github.com/Zakk-Yang/ollama-rag.git
   cd my_llama_project
   ```

2. **Create a Virtual Environment (Recommended)**
    ```bash
    conda create -n env python=3.10
    conda activate env
    ```

3. **Install Dependencies and the Package**
    ```bash
    pip install .
    ```
    
4. **Install Ollama model**
Please visit https://ollama.com/download for more details.
Install your selected model by the following example: 
```bash
ollama pull llama3.2
```

## Usage
### Running a Query
```python
from ollama_rag import OllamaRAG

# Initialize the query engine with your configurations
engine = OllamaRAG(
    model_name="llama3.2", # replace your ollama model name
    request_timeout=120.0,
    embedding_model_name="BAAI/bge-large-en-v1.5", # replace your hugging face embedding model
    trust_remote_code=True,
    input_dirs=[
        "/your/path/to/your/documents",
        # Add more directories as needed
    ],
    required_exts=[
        ".txt", ".md", ".html", ".htm", ".xml", ".json", ".csv",
        ".pdf", ".doc", ".docx", ".rtf", ".ipynb",
    ]
)

# Update the index with new or updated documents
engine.update_index()

# Run a query
response = engine.query("where can i find Jason Black's address?") # replace your question
print(response)
```


## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the Repository
2. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

3. Commit Your Changes
```bash
git commit -am 'Add new feature'
```
4.Push to the Branch
```bash
git push origin feature/your-feature-name
```

## License
The source code for the site is licensed under the MIT license, which you can find in the MIT-LICENSE.txt file.