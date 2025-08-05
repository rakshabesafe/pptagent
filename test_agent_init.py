from core.agent import RAGAgent
import time

def test_agent_init():
    print("Creating RAG agent...")
    start_time = time.time()
    try:
        agent = RAGAgent()
        print("RAG agent created successfully.")
    except Exception as e:
        print(f"Error creating RAG agent: {e}")
    end_time = time.time()
    print(f"RAG agent creation took {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    test_agent_init()
