from core.extractor import extract_metadata
from core.agent import RAGAgent
import time

def test_backend():
    # 1. Create a test PPT file (or use the existing one)
    # (Assuming test.pptx exists from previous steps)

    # 2. Extract metadata
    print("Extracting metadata...")
    start_time = time.time()
    metadata = extract_metadata("test.pptx")
    end_time = time.time()
    print(f"Metadata extraction took {end_time - start_time:.2f} seconds.")
    print(f"Extracted metadata for {len(metadata)} slides.")

    # 3. Create a RAG agent and add documents
    print("Creating RAG agent...")
    start_time = time.time()
    agent = RAGAgent()
    end_time = time.time()
    print(f"RAG agent creation took {end_time - start_time:.2f} seconds.")

    print("Adding documents to the agent...")
    start_time = time.time()
    agent.add_documents(metadata, "test.pptx")
    end_time = time.time()
    print(f"Adding documents took {end_time - start_time:.2f} seconds.")
    print("Documents added to the agent.")

    # 4. Perform a search
    query = "Python"
    print(f"Searching for: '{query}'")
    start_time = time.time()
    results = agent.search(query)
    end_time = time.time()
    print(f"Search took {end_time - start_time:.2f} seconds.")

    print("Search results:")
    for result in results:
        doc, score = result
        print(f"  File: {doc.metadata['ppt_filename']}, Slide: {doc.metadata['slide_number']} (Score: {score:.4f})")
        print(f"  Content: {doc.page_content}")
        print("-" * 20)

if __name__ == "__main__":
    test_backend()
