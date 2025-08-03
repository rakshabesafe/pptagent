from qdrant_client import QdrantClient
from core import config
import time

def test_qdrant_connection():
    print("Connecting to Qdrant...")
    start_time = time.time()
    try:
        client = QdrantClient(host=config.QDRANT_HOST, port=config.QDRANT_PORT)
        print("Qdrant client created successfully.")
        # Perform a simple operation to check the connection
        client.get_collections()
        print("Successfully connected to Qdrant.")
    except Exception as e:
        print(f"Error connecting to Qdrant: {e}")
    end_time = time.time()
    print(f"Qdrant connection test took {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    test_qdrant_connection()
