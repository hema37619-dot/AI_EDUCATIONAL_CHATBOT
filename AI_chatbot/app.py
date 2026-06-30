import streamlit as st
from rag.retriever import get_retriever
import requests
from groq import Groq
import os

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Educational Chatbot",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7ff;
}

.title {
    font-size: 45px;
    font-weight: bold;
    color: #4B0082;
    text-align: center;
}

.subtitle {
    font-size: 20px;
    color: #4B0082;
    text-align: center;
    margin-bottom: 30px;
}

.stTextInput > div > div > input {
    background-color: #ffffff;
    border: 2px solid #4B0082;
    border-radius: 10px;
    padding: 10px;
    font-size: 18px;
    color: black;
}

.context-box {
    background-color: #E8F0FE;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
    color: black;
}

.answer-box {
    background-color: #E8F0FE;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
    color: black;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown(
    '<p class="title">AI Educational Chatbot</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Ask Questions from Your PDF Notes using RAG + AI</p>',
    unsafe_allow_html=True
)

# -------------------------------
# Load Retriever
# -------------------------------
@st.cache_resource
def load_retriever():
    return get_retriever()

retriever = load_retriever()

# -------------------------------
# Question Input
# -------------------------------
question = st.text_input("📌 Enter your question:")

# -------------------------------
# Process Question
# -------------------------------
if question:

    try:
        # Retrieve Documents
        with st.spinner("🔍 Searching documents..."):
            docs = retriever.invoke(question)

            context = ""
            for doc in docs[:3]:
                context += doc.page_content[:500] + "\n\n"

        # Show Context
        st.subheader("📚 Retrieved Context")
        st.markdown(
            f'<div class="context-box">{context}</div>',
            unsafe_allow_html=True
        )

        # Build Prompt
        prompt = f"""You are an educational assistant. Your job is to answer student questions strictly based on the study material provided below.

Rules:
- Answer ONLY using the context provided. Do NOT use your own training knowledge.
- If the answer is not present in the context, respond with: "This topic is not covered in the provided study material."
- Be concise and clear.

Context:
{context}

Question: {question}

Answer:"""

        # Generate Answer via Groq
        with st.spinner("🤖 Generating answer..."):
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content.strip()

        # Display Answer
        st.subheader("🤖 Answer")
        st.markdown(
            f'<div class="answer-box">{answer}</div>',
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Error: {str(e)}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown(
    "<center>Built with ❤️ Streamlit + LangChain + Groq + ChromaDB</center>",
    unsafe_allow_html=True
)
