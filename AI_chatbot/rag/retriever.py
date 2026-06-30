from langchain_community.vectorstores import Chroma
from rag.embedding import get_embedding_model
def get_retriever():
    #load the embedding model
    embedding_model=get_embedding_model()
    #load chroma database
    db=Chroma(
        persist_directory='chroma_db',
        embedding_function=embedding_model
    )
    #create retriever
    retriever=db.as_retriever(search_kwargs={'k':3})
    return retriever