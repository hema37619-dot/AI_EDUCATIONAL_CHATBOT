from langchain_community.document_loaders import TextLoader
import os
def load_documents():
    docs=[]
    for file in os.listdir("data"):
        loader=TextLoader(
            f"data/{file}"
        )
        docs.extend(loader.load())
    return docs