# PPT AI Agent

This project is a Retrieval-Augmented Generation (RAG) agent for PowerPoint files. It allows users to upload `.pptx` files, extracts metadata (text and images), stores it in a vector database, and provides a semantic search interface.

## Architecture

The application is composed of the following components:

-   **Streamlit UI**: A web interface for file uploading and search.
-   **Backend Orchestration**: Uses LangGraph to coordinate file processing and RAG search.
-   **Metadata Extraction**: Python scripts to extract text, images, and comments from PPT files.
-   **Vector Database**: Qdrant is used for storing and searching vectorized metadata.
-   **Storage**: A local `files` directory is used to store the uploaded PPT files.

# Architecture for PPT RAG Agent

This design outlines a Retrieval-Augmented Generation (RAG) agent for PowerPoint file upload, metadata extraction, vector storage, and semantic search—implemented with Streamlit and LangGraph.

## 1. PPT Upload and Vector Store Workflow

### Overview
- **Frontend:** Streamlit app for file upload and search interface.
- **Backend Orchestration:** LangGraph coordinates file processing and RAG search.
- **Storage:** Uploaded PPT files saved to disk; metadata stored in a vector database for retrieval.

### Steps

#### A. File Upload (Streamlit)
- Users upload `.pptx` files through a Streamlit file uploader widget.
- Files are temporarily held in memory, processed, then stored in a designated folder for later retrieval.

#### B. Metadata Extraction (Backend Processing)
For each uploaded PPT file:
- **a. Extract Text:** Read all textual content from slides using Python libraries like `python-pptx`.
- **b. Slide as Image:** Render each slide as an image (to capture visual diagrams/architectures), process these images (e.g., OCR or image embeddings for diagrams).
- **c. Extract Comments:** Parse slide comments using libraries like `win32com` on Windows or by unzipping the `.pptx` to read the underlying XML.
- Compile a unified metadata object containing:
  - Slide texts
  - Image-based embeddings
  - Comments and notes

#### C. Vector Database Storage
- Extracted metadata (text, image embeddings, comments) is chunked and converted to vector embeddings using an embedding model.
- Store these embeddings along with metadata in the vector database (e.g., Pinecone, Qdrant, Weaviate, Milvus).
- Persist the original PPT file in a local (or cloud) storage folder.

## 2. Semantic Search with Rational Explanation

### A. User Query (via Streamlit)
- User inputs a natural language query.

### B. RAG Pipeline (LangGraph Orchestration)
- The natural language query is embedded and sent to the vector database to perform similarity search across all stored PPT metadata.
- Retrieve a ranked list of relevant PPT files, with each result accompanied by a rational explanation—why the file is related (e.g., matching text, similar architecture diagram, relevant comments).
- Optionally, provide runners-up with lower relevance scores and their rationales.

## Component Interaction Diagram

| Component         | Description                                                                                 |
|-------------------|---------------------------------------------------------------------------------------------|
| Streamlit UI      | For file upload, search input, and results display.                                         |
| Metadata Extract  | Python functions (called by LangGraph) to process PPT files and extract all metadata types. |
| Vector DB         | Stores embeddings and metadata for semantic search.                                         |
| Storage Folder    | Persistent storage for raw PPT files.                                                       |
| LangGraph Flow    | Orchestrates processing (on ingestion) and querying (on search).                            |

## Technologies/Frameworks

- **Streamlit:** For the web interface for upload/search.
- **LangGraph:** Orchestration of ingestion and search workflows.
- **python-pptx, PIL, OCR:** For reading and rendering PPT content.
- **Vector DBs:** Pinecone, Qdrant, or Weaviate for fast vector search.
- **Storage:** File system or S3 for PPT files.

## High-Level Flow

1. **Upload:** User uploads a PPT file through the app.
2. **Process:**
    - Extract text from slides.
    - Render images from slides and (optionally) run OCR/embedding models.
    - Extract comments/notes.
3. **Store:**
    - Save the vectorized metadata to the vector database.
    - Save the original PPT to storage.
4. **Search:**
    - User submits a query.
    - System retrieves and ranks matching PPTs from the vector DB.
    - Shows results with rationales.

## Example Pseudocode for Core Steps

```python
# Streamlit upload
uploaded_file = st.file_uploader("Upload PPT", type=["pptx"])
if uploaded_file:
    save_to_storage(uploaded_file)
    metadata = extract_all_metadata(uploaded_file)
    store_in_vector_db(metadata)

# Search
query = st.text_input("Search PPTs")
if query:
    results = langgraph_rag_search(query)
    st.write(results)
```

## Key Considerations

- **Metadata Coverage:** Ensure text, image, and comments are all captured to maximize search accuracy.
- **Vector Storage Efficiency:** Be prepared for storage overhead (vector representations may be 10x larger than original text).
- **Scalability:** Use a vector DB that fits scale/performance requirements; optimize for relevant real-world queries.


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
