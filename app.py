import streamlit as st

st.set_page_config(
    page_title="Automatic Tag Generator",
    page_icon="🏷️",
    layout="centered"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
}
.big-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🏷️ Automatic Tag Generator</p>',
            unsafe_allow_html=True)

st.markdown('<p class="subtitle">Generate smart hashtags instantly ✨</p>',
            unsafe_allow_html=True)

text = st.text_area(
    "Enter your content",
    placeholder="Type your text here..."
)

if st.button("🚀 Generate Tags"):
    words = text.split()
    tags = ["#" + word.capitalize() for word in words]

    st.success("Tags Generated Successfully!")

    st.markdown("### 🎯 Suggested Tags")

    for tag in tags:
        st.markdown(f"🔹 **{tag}**")