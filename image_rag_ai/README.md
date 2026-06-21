# AI Image Generator

A text-to-image generation system that uses RAG (Retrieval-Augmented Generation) to automatically select the best art style for your prompt and generate high-quality images using Stable Diffusion.

## What It Does
- User enters a text prompt (e.g. "a girl sitting in a garden")
- RAG retrieves the most relevant art style from a style knowledge base
- The style is combined with the prompt to create an enhanced final prompt
- Stable Diffusion generates the image based on the final prompt

## How It Works
1. Art styles are loaded from `styles.txt` and stored in ChromaDB as embeddings
2. When a prompt is entered, the most semantically similar style is retrieved (k=1)
3. The retrieved style is appended to the user prompt
4. Stable Diffusion generates the image from the enhanced prompt

## Tech Stack
- Streamlit — UI
- LangChain — RAG pipeline
- ChromaDB — vector store
- HuggingFace Embeddings — all-MiniLM-L6-v2
- Stable Diffusion (runwayml/stable-diffusion-v1-5) — image generation

## Project Structure
```
image_rag_ai/
├── app.py                      # Streamlit app
├── rag/
│   ├── loader.py               # Style document loader
│   ├── embedding.py            # HuggingFace embedding model
│   ├── vector_store.py         # ChromaDB vector store
│   └── retriever.py            # Style retriever
├── image_generation/
│   └── generator.py            # Stable Diffusion image generator
├── data/
│   └── styles.txt              # Art style knowledge base
└── chroma_db/                  # Auto-generated vector store
```

## Setup & Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Available Art Styles
- Realistic — Photorealistic, 8K UHD, Professional photography
- Animal / Studio Ghibli — Large expressive eyes, Vibrant colors
- Fantasy — Magical environment, Mystical creatures
- Cyberpunk — Neon lights, Futuristic city
- Cartoon — Disney inspired, Bright colors
- Watercolor — Soft brush strokes, Pastel colors
- Pixar — 3D rendered, Movie-quality lighting
