# AI Educational Chatbot

An intelligent educational assistant that answers student questions based strictly on uploaded PDF study materials using RAG (Retrieval-Augmented Generation).

## What It Does
- Upload your PDF notes or study material
- Ask any question related to the content
- The chatbot retrieves relevant context from the PDFs and answers using only that content
- If the answer is not in the PDFs, it responds: "This topic is not covered in the provided study material"

## How It Works
1. PDFs are loaded and split into chunks
2. Chunks are embedded using HuggingFace (all-MiniLM-L6-v2) and stored in ChromaDB
3. When a question is asked, the top 3 relevant chunks are retrieved
4. Llama3 (via Ollama) generates an answer strictly based on the retrieved context

## Tech Stack
- Streamlit — UI
- LangChain — RAG pipeline
- ChromaDB — vector store
- HuggingFace Embeddings — all-MiniLM-L6-v2
- Ollama (Llama3) — LLM
- PyPDF — PDF loading

## Project Structure
```
aichatbot/
├── app.py                  # Streamlit app
├── utils/
│   ├── embedding.py        # HuggingFace embedding model
│   ├── retriever.py        # ChromaDB retriever
│   ├── loader.py           # PDF loader
│   └── splitter.py         # Text splitter
├── data/                   # Place your PDF files here
└── chroma_db/              # Auto-generated vector store
```

## Setup & Run
```bash
# Install dependencies
pip install -r requirements.txt

# Start Ollama
ollama serve
ollama pull llama3

# Add your PDFs to the data/ folder

# Run the app
streamlit run app.py
```
