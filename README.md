# AI Educational Chatbot & Image Generator

This repository contains two AI projects built using RAG (Retrieval-Augmented Generation), LangChain, ChromaDB, and Streamlit.

---

## Projects

### 1. AI Educational Chatbot
An intelligent chatbot that answers student questions strictly based on uploaded PDF study materials. It uses RAG to retrieve relevant content from PDFs and generates answers using Llama3 via Ollama — ensuring responses come only from the provided material, not from general AI knowledge.

### 2. AI Image Generator
A text-to-image generation system that uses RAG to retrieve the most relevant art style from a style knowledge base and combines it with the user's prompt to generate high-quality images using Stable Diffusion.

---

## Tech Stack
- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings (all-MiniLM-L6-v2)
- Ollama (Llama3)
- Stable Diffusion
- PyPDF

---

## Project Structure
```
AI_EDUCATIONAL_CHATBOT/
├── aichatbot/        # RAG-based educational chatbot
└── image_rag_ai/     # RAG-based AI image generator
```
