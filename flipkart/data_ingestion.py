from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from flipkart.data_converter import DataConverter
from flipkart.config import Config

class DataIngestor:
    def __init__(self):
        self.embedding = HuggingFaceEndpointEmbeddings(model=Config.EMBEDDING_MODEL)
        self.vector_store = AstraDBVectorStore(
            collection_name=Config.ASTRA_DB_COLLECTION,
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            embedding=self.embedding,
            namespace=Config.ASTRA_DB_KEYSPACE
        )
    
    def ingest(self, load_existing: bool = False):
        if load_existing:
            print("Loading existing data from AstraDB...")
            return self.vector_store

        print("Converting data from CSV...")
        docs = DataConverter(file_path="data/flipkart_product_review.csv").convert()
        self.vector_store.add_documents(docs)
        
        return self.vector_store