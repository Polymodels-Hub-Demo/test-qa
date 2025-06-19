import streamlit as st

st.set_page_config(page_title="File Uploader & Downloader", layout="centered")

st.title("📤 Upload & 📥 Download Your File")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=None)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    # Display download button
    st.download_button(
        label="📥 Download your file",
        data=uploaded_file.getvalue(),
        file_name=uploaded_file.name,
        mime=uploaded_file.type or "application/octet-stream",
    )
