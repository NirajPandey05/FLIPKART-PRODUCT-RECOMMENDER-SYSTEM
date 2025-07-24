import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
    ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
    ASTRA_DB_COLLECTION = os.getenv("ASTRA_DB_COLLECTION")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    HF_TOKEN = os.getenv("HF_TOKEN")
    HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    EMBEDDING_MODEL = os.getenv("HUGGINGFACE_EMBEDDINGS_MODEL", "BAAI/bge-base-en-v1.5")
    RAG_MODEL = "llama-3.1-8b-instant"
