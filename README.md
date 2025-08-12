# PPT AI Agent

This project is a Retrieval-Augmented Generation (RAG) agent for PowerPoint files. It allows users to upload `.pptx` files, extracts metadata (text and images), stores it in a vector database, and provides a semantic search interface.

## Architecture

The application is composed of the following components:

-   **Streamlit UI**: A web interface for file uploading and search.
-   **Backend Orchestration**: Uses LangGraph to coordinate file processing and RAG search.
-   **Metadata Extraction**: Python scripts to extract text, images, and comments from PPT files.
-   **Vector Database**: Qdrant is used for storing and searching vectorized metadata.
-   **Storage**: A local `files` directory is used to store the uploaded PPT files.

### High-Level Flow

1.  **Upload**: A user uploads a PPT file through the Streamlit application.
2.  **Process**: The backend extracts text and images from the slides.
3.  **Store**: The extracted metadata is vectorized and stored in the Qdrant vector database. The original PPT file is saved to the `files` directory.
4.  **Search**: The user submits a query through the Streamlit interface. The system retrieves and ranks matching PPTs from the vector database and displays the results.

## Requirements

The following Python libraries are required to run the application:

```
streamlit
langchain
python-pptx
Pillow
pytesseract
qdrant-client
fastembed
```

## Deployment

To deploy and run the application, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit application**:
    ```bash
    streamlit run src/main.py
    ```

4.  **Access the application**: Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).