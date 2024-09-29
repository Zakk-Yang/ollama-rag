# Llama Index Query Engine + Ollama Model to Create Your Own Knowledge Pool

This project is a robust and modular application that builds an efficient query engine using LlamaIndex, ChromaDB, and custom embeddings. It allows you to index documents from multiple directories and query them using natural language.

Input Question Example: where can i find the adress of Jason Black?
Output example: The address is 'xxx, xxx, xxx'



## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
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
my_llama_project/
├── main.py
├── models.py
├── data_loader.py
├── indexer.py
├── query_engine.py
├── prompts.py
├── configs.py            # Updated config file with multiple INPUT_DIRS
├── document_tracker.py   # New module for tracking indexed files
├── requirements.txt
├── storage/              # Directory for persisted index data (created automatically if missing)
├── chroma_db/            # Directory for ChromaDB data (created automatically if missing)
├── indexed_files.json    # Indexed files metadata (auto-created if missing)
└── documents/            # Directory containing the documents to be indexed

```

## Prerequisites

- **Python 3.7 or higher**: Ensure you have Python installed.
- **Git**: For cloning the repository.
- **Pip**: Python package installer.

## Installation

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

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Install Ollama model**
Please visit https://ollama.com/download for more details.
Install your selected model by the following example: 
```bash
ollama pull llama3.2
```

## Configuration
1. **Configure Input Directories**
Open configs.py and update the INPUT_DIRS list with the paths to your document directories.
```python
INPUT_DIRS = [
    '/your/path/to/your/document1',
    '/your/path/to/your/document2',
    # Add more directories as needed
]
```
2. **Model Name and Other Path Locations**


## Usage
1. Run the Application
```bash
python main.py
```

2.Running with a Custom Query

```bash
python main.py --query "Your custom query here"
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