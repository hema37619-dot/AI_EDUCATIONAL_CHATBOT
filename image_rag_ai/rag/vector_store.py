from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
def create_vector_store(docs, embedding):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=0,
        separators=["\n\n"]
    )
    chunks = splitter.split_documents(docs)
    
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="chroma_db"
    )
    return vectordb