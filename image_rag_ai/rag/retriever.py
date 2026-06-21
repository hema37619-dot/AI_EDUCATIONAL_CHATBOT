from rag.loader import load_documents
from rag.embedding import get_embedding
from rag.vector_store import create_vector_store

def retrieve_context(query):
    docs = load_documents()
    embedding = get_embedding()
    db = create_vector_store(docs, embedding)

    retriever = db.as_retriever(search_kwargs={"k": 1})
    results = retriever.invoke(query)

    print("RAW RESULTS:", results)

    context = results[0].page_content if results else ""
    print("CONTEXT:", repr(context))
    return context