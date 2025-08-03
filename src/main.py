import streamlit as st
from core.utils import save_uploaded_file
from core.extractor import extract_metadata
from core.agent import RAGAgent

def main():
    st.set_page_config(page_title="PPT AI Agent", page_icon="🤖")
    st.title("PPT AI Agent")

    if "agent" not in st.session_state:
        st.session_state.agent = RAGAgent()

    st.subheader("Upload a PowerPoint file")
    uploaded_file = st.file_uploader("Choose a .pptx file", type=["pptx"])

    if uploaded_file is not None:
        file_path = save_uploaded_file(uploaded_file)
        if file_path:
            st.success(f"File '{uploaded_file.name}' uploaded and saved successfully!")
            metadata = extract_metadata(file_path)
            st.session_state.agent.add_documents(metadata, uploaded_file.name)
            st.info("File processed and indexed.")

    st.subheader("Search for information")
    query = st.text_input("Enter your search query")

    if st.button("Search"):
        if query:
            st.info(f"Searching for: '{query}'")
            results = st.session_state.agent.search(query)
            for result in results:
                doc, score = result
                st.write(f"**File:** {doc.metadata['ppt_filename']}, **Slide:** {doc.metadata['slide_number']} (Score: {score:.4f})")
                st.write(doc.page_content)
                st.write("---")
        else:
            st.warning("Please enter a search query.")

if __name__ == "__main__":
    main()
