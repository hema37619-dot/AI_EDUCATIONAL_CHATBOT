from langchain_community.document_loaders import PyPDFLoader
import os
def load_all_pdfs(data_folder='data'):
    documents = []
    for file in os.listdir(data_folder):
        if file.endswith('.pdf'):
            pdf_path = os.path.join(data_folder, file)
            loader = PyPDFLoader(pdf_path)
            docs=loader.load()
            documents.extend(docs)
    return documents