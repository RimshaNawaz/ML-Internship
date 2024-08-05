
import chromadb

def initialize_client():
    """Initialize ChromaDB client and create or get a collection."""
    client = chromadb.Client()
    collection_name = 'disease_symptoms'
    collection = client.create_collection(name=collection_name)
    return collection
