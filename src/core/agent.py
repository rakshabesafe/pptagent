import os
from qdrant_client import QdrantClient, models
from fastembed import FastEmbed
from langchain.vectorstores import Qdrant
from langchain.schema import Document

class RAGAgent:
    def __init__(self):
        self.client = QdrantClient(":memory:")
        self.embedding_model = FastEmbed()
        self.collection_name = "ppt_collection"
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
        )
        self.vector_store = Qdrant(
            client=self.client,
            collection_name=self.collection_name,
            embeddings=self.embedding_model,
        )

    def add_documents(self, metadata_list, ppt_filename):
        documents = []
        for metadata in metadata_list:
            doc_content = f"Slide {metadata['slide_number']}\n"
            doc_content += f"Text: {metadata['text']}\n"
            doc_content += f"OCR Text: {metadata['ocr_text']}"

            doc = Document(
                page_content=doc_content,
                metadata={
                    "ppt_filename": ppt_filename,
                    "slide_number": metadata["slide_number"],
                },
            )
            documents.append(doc)

        self.vector_store.add_documents(documents)

    def search(self, query, k=3):
        return self.vector_store.similarity_search_with_score(query, k=k)
