This package will be replaced by https://github.com/Zakk-Yang/nexusync


# Llama Index Query Engine + Ollama Model to Create Your Own Knowledge Pool

This project is a robust and modular application that builds an efficient query engine using LlamaIndex, ChromaDB, and custom embeddings. It allows you to index documents from multiple directories and query them using natural language. You can connect to any local folders, and of course, you can connect OneDrive and iCloud folders.



## Table of Contents

- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Usage
### Running a Query
```python
from ollama_rag import OllamaRAG

# Initialize the query engine with your configurations
engine = OllamaRAG(
    model_name="llama3.2",  # Replace with your Ollama model name
    request_timeout=120.0,
    embedding_model_name="BAAI/bge-large-en-v1.5",  # Replace with your Hugging Face embedding model
    trust_remote_code=True,
    input_dirs=[
        "/your/path/to/your/documents",
        # Add more directories as needed
        # if you are in wsl environment, make sure your path is like "/mnt/c/..."
        # if you are in windows, use r"C:\Users\<YourUsername>\Documents", etc
        # if you are in mac, use   "/Users/<YourUsername>/Documents", etc
        # if you want to find obsidian notes, find "iCloud~md~obsidian" in your icloud. Or you find it in your local.
    ],
    required_exts=[
        ".txt", ".md", ".html", ".htm", ".xml", ".json", ".csv",
        ".pdf", ".doc", ".docx", ".rtf", ".ipynb",
        ".ppt", ".pptx", ".xls", ".xlsx",  # you can remove required_exts by default to capture all supported extentions
    ]
)

# Update the index with new or updated documents
engine.update_index()

# Run a query
response = engine.query("can LLM generate creative contents?")
print(response)

```
Ouptut is a dict:

```text
{'response': "Yes, the text suggests that LLMs (Large Language Models) can generate novel research ideas and even outperform human experts in terms of novelty. The authors claim that their AI agent generates ideas that are statistically more novel than those written by expert researchers. However, it's worth noting that the effectiveness of LLMs in generating creative content is a topic of ongoing debate, and not all studies have found similar results (e.g., Chakrabarty et al. (2024) found that AI writings are less creative than professional writers). Nevertheless, based on the provided context, it appears that LLMs can generate novel research ideas under certain conditions.",
  'sources': [
      {'document_id': 'Can LLMs Generate Novel Research Ideas.pdf',
      'file_path': '/mnt/d/Paper/Can LLMs Generate Novel Research Ideas.pdf', 
      'page_number': '18', 
      'sheet_name': 'N/A',
      'text_snippet': '9 Related Work\nResearch idea generation and execution . Several prior works explored methods to improve idea\ngeneration, such as iterative novelty boosting (Wang et al., 2024), multi-agent collaborati...'}
      ]
}
```


## Features


- **Modular Design**: The project is organized into separate modules for easy maintenance and scalability.
- **Efficient Indexing**: Uses ChromaDB to store embeddings, allowing efficient indexing and querying.
- **Incremental Updates**: Only new or updated documents are indexed, improving performance.
- **Multiple Directories Support**: Indexes documents from multiple directories across different locations.
- **Custom Embeddings**: Utilizes custom embedding models for better performance.
- **Error Handling**: Gracefully handles missing directories or files and recreates the index as needed.
- **Logging**: Provides detailed logs for monitoring and debugging.
- **Advanced Text-Based File Support**: Supports a variety of text-based file formats, including:
    ".txt",
    ".md",
    ".html",
    ".htm",
    ".xml",
    ".json",
    ".csv",
    ".pdf",
    ".doc",
    ".docx",
    ".rtf",
    ".ipynb",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",

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
- **ollama**: https://ollama.com/download, install your selected model by the following example: 
```bash
ollama pull llama3.2
```
- **LibreOffice**:

Required for converting .ppt files to .pptx when processing PowerPoint files. 
After conversion, I suggest you delete the ppt as it will always be converted and re-indexed again.
Ubuntu/Debian:
```bash
sudo apt update
sudo apt install libreoffice
```
macOS (using Homebrew):
```bash
brew install --cask libreoffice
```
Windows:
Download and install from the LibreOffice official website https://www.libreoffice.org/download/download-libreoffice/.





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
