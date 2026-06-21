import streamlit as st
from rag.retriever import retrieve_context
from image_generation.generator import generate_image

# PAGE CONFIG
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🧈",
    layout="wide"
)

st.markdown("""
<style>
.main{
    background: linear-gradient(135deg, #0f172a, #1e293b);
}
.title {
    text-align:center;
    font-size:50px;
    font-weight:bold;
}
.subtitle{
    text-align:center;
    font-size:20px;
    color:white;
    margin-bottom:30px;
}
.stButton>button{
    width:100%;
    background:linear-gradient(90deg, #06b6d4, #3b82f6);
    color:white;
    font-size:18px;
    font-weight:bold;
    border-radius:18px;
    height:50px;
}
.result-card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 40px 20px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<div class="title">❄️ AI Image Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate Stunning AI Images using RAG + Stable Diffusion</div>', unsafe_allow_html=True)

# LAYOUT
left, right = st.columns([1, 1])

with left:
    st.subheader("🎹 Enter Prompt")
    prompt = st.text_area(
        "",
        height=150,
        placeholder="Example: Create a futuristic city with flying cars and neon lights..."
    )
    generate_btn = st.button("🛩️ Generate Image")

with right:
    st.subheader("✨ Generated Result")
    if generate_btn and prompt:
        with st.spinner("Creating masterpiece..."):
            context = retrieve_context(prompt)
            final_prompt = f"{prompt}, {context}"

        st.markdown(f"**Prompt:** {prompt}")
        st.markdown(f"**Retrieved Style:** {context}")
        st.markdown(f"**Final Prompt:** {final_prompt}")

        with st.spinner("Generating image..."):
            result = generate_image(final_prompt)
            st.image(result, caption="Generated Image", use_container_width=True)
