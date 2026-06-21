from utils.loader import load_all_pdfs
from utils.splitter import split_documents
from utils.embedding import get_embedding_model
from langchain_community.vectorstores import Chroma

print("Loading PDFs...")

documents = load_all_pdfs()

print(f"loaded {len(documents)} pages")
print("splitting documnets..")

chunks = split_documents(documents)
print(f"created {len(chunks)} chunks")
print("loading embedding model...")
embedding_model = get_embedding_model()
print("creating chromaDB vector store...")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)
vectorstore.persist()
print("embeddings stored successfully !")