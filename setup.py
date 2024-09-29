# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ollama_rag",
    version="0.2.4",
    author="Zakk Yang",
    author_email="zakkyang@protonmail.com",
    description="A RAG (Retrieval-Augmented Generation) system using Llama Index and ChromaDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zakk-Yang/ollama-rag.git",  # Replace with your repository URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "aiohappyeyeballs==2.4.2",
        "aiohttp==3.10.8",
        "aiosignal==1.3.1",
        "annotated-types==0.7.0",
        "anyio==4.6.0",
        "asgiref==3.8.1",
        "async-timeout==4.0.3",
        "asyncpg==0.29.0",
        "attrs==24.2.0",
        "autocommand==2.2.2",
        "backoff==2.2.1",
        "backports.tarfile==1.2.0",
        "bcrypt==4.2.0",
        "beautifulsoup4==4.12.3",
        "build==1.2.2",
        "cachetools==5.5.0",
        "certifi==2024.8.30",
        "cffi==1.17.1",
        "charset-normalizer==3.3.2",
        "chroma-hnswlib==0.7.6",
        "chromadb==0.5.11",
        "click==8.1.7",
        "coloredlogs==15.0.1",
        "cryptography==43.0.1",
        "dataclasses-json==0.6.7",
        "Deprecated==1.2.14",
        "dirtyjson==1.0.8",
        "distro==1.9.0",
        "docutils==0.21.2",
        "durationpy==0.7",
        "fastapi==0.115.0",
        "filelock==3.16.1",
        "flatbuffers==24.3.25",
        "frozenlist==1.4.1",
        "fsspec==2024.9.0",
        "google-auth==2.35.0",
        "googleapis-common-protos==1.65.0",
        "greenlet==3.1.1",
        "grpcio==1.66.2",
        "h11==0.14.0",
        "httpcore==1.0.5",
        "httptools==0.6.1",
        "httpx==0.27.2",
        "huggingface-hub==0.25.1",
        "humanfriendly==10.0",
        "idna==3.10",
        "importlib_metadata==8.4.0",
        "importlib_resources==6.4.5",
        "inflect==7.3.1",
        "jaraco.classes==3.4.0",
        "jaraco.collections==5.1.0",
        "jaraco.context==5.3.0",
        "jaraco.functools==4.0.1",
        "jaraco.text==3.12.1",
        "jeepney==0.8.0",
        "Jinja2==3.1.4",
        "jiter==0.5.0",
        "joblib==1.4.2",
        "keyring==25.4.1",
        "kubernetes==31.0.0",
        "llama-cloud==0.1.0",
        "llama-index==0.11.14",
        "llama-index-agent-openai==0.3.4",
        "llama-index-cli==0.3.1",
        "llama-index-core==0.11.14",
        "llama-index-embeddings-huggingface==0.3.1",
        "llama-index-embeddings-openai==0.2.5",
        "llama-index-indices-managed-llama-cloud==0.4.0",
        "llama-index-legacy==0.9.48.post3",
        "llama-index-llms-ollama==0.3.3",
        "llama-index-llms-openai==0.2.9",
        "llama-index-multi-modal-llms-openai==0.2.1",
        "llama-index-program-openai==0.2.0",
        "llama-index-question-gen-openai==0.2.0",
        "llama-index-readers-file==0.2.2",
        "llama-index-readers-llama-parse==0.3.0",
        "llama-index-vector-stores-chroma==0.2.0",
        "llama-index-vector-stores-postgres==0.2.5",
        "llama-parse==0.5.6",
        "markdown-it-py==3.0.0",
        "MarkupSafe==2.1.5",
        "marshmallow==3.22.0",
        "minijinja==2.2.0",
        "mmh3==5.0.1",
        "monotonic==1.6",
        "more-itertools==10.3.0",
        "mpmath==1.3.0",
        "multidict==6.1.0",
        "mypy-extensions==1.0.0",
        "networkx==3.3",
        "nh3==0.2.18",
        "nltk==3.9.1",
        "numpy==1.26.4",
        "nvidia-cublas-cu12==12.1.3.1",
        "nvidia-cuda-cupti-cu12==12.1.105",
        "nvidia-cuda-nvrtc-cu12==12.1.105",
        "nvidia-cuda-runtime-cu12==12.1.105",
        "nvidia-cudnn-cu12==9.1.0.70",
        "nvidia-cufft-cu12==11.0.2.54",
        "nvidia-curand-cu12==10.3.2.106",
        "nvidia-cusolver-cu12==11.4.5.107",
        "nvidia-cusparse-cu12==12.1.0.106",
        "nvidia-nccl-cu12==2.20.5",
        "nvidia-nvjitlink-cu12==12.6.68",
        "nvidia-nvtx-cu12==12.1.105",
        "oauthlib==3.2.2",
        "ollama==0.3.3",
        "onnxruntime==1.19.2",
        "openai==1.50.2",
        "opentelemetry-api==1.27.0",
        "opentelemetry-exporter-otlp-proto-common==1.27.0",
        "opentelemetry-exporter-otlp-proto-grpc==1.27.0",
        "opentelemetry-instrumentation==0.48b0",
        "opentelemetry-instrumentation-asgi==0.48b0",
        "opentelemetry-instrumentation-fastapi==0.48b0",
        "opentelemetry-proto==1.27.0",
        "opentelemetry-sdk==1.27.0",
        "opentelemetry-semantic-conventions==0.48b0",
        "opentelemetry-util-http==0.48b0",
        "orjson==3.10.7",
        "overrides==7.7.0",
        "pandas==2.2.3",
        "pgvector==0.2.5",
        "pillow==10.4.0",
        "pkginfo==1.10.0",
        "posthog==3.6.6",
        "protobuf==4.25.5",
        "psycopg2-binary==2.9.9",
        "pyasn1==0.6.1",
        "pyasn1_modules==0.4.1",
        "pycparser==2.22",
        "pydantic==2.9.2",
        "pydantic_core==2.23.4",
        "pypdf==4.3.1",
        "PyPika==0.48.9",
        "pyproject_hooks==1.2.0",
        "python-dotenv==1.0.1",
        "pytz==2024.2",
        "PyYAML==6.0.2",
        "readme_renderer==44.0",
        "regex==2024.9.11",
        "requests==2.32.3",
        "requests-oauthlib==2.0.0",
        "requests-toolbelt==1.0.0",
        "rfc3986==2.0.0",
        "rich==13.8.1",
        "rsa==4.9",
        "safetensors==0.4.5",
        "scikit-learn==1.5.2",
        "scipy==1.14.1",
        "SecretStorage==3.3.3",
        "sentence-transformers==3.1.1",
        "shellingham==1.5.4",
        "sniffio==1.3.1",
        "soupsieve==2.6",
        "SQLAlchemy==2.0.35",
        "starlette==0.38.6",
        "striprtf==0.0.26",
        "sympy==1.13.3",
        "tenacity==8.5.0",
        "threadpoolctl==3.5.0",
        "tiktoken==0.7.0",
        "tokenizers==0.20.0",
        "tomli==2.0.1",
        "torch==2.4.1",
        "tqdm==4.66.5",
        "transformers==4.45.1",
        "triton==3.0.0",
        "twine==5.1.1",
        "typeguard==4.3.0",
        "typer==0.12.5",
        "typing-inspect==0.9.0",
        "tzdata==2024.2",
        "urllib3==2.2.3",
        "uvicorn==0.31.0",
        "uvloop==0.20.0",
        "watchfiles==0.24.0",
        "websocket-client==1.8.0",
        "websockets==13.1",
        "wrapt==1.16.0",
        "yarl==1.13.1",
    ],
    include_package_data=True,  # Ensures files specified in MANIFEST.in are included
    entry_points={
        "console_scripts": [
            "ollama-rag=ollama_rag.ollama_rag:main",  # Points to the standalone main function
        ],
    },
)
