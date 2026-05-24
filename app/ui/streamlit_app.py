import streamlit as st
import requests

API_URL = "https://web-production-c1b1e.up.railway.app"

st.set_page_config(page_title="Enterprise AI Agent Platform")

st.title("Enterprise AI Agent Platform")
st.write("Document-based AI workflow with OpenAI integration.")

st.subheader("Upload Document")

uploaded_file = st.file_uploader(
    "Upload a PDF or TXT file",
    type=["pdf", "txt"]
)

if uploaded_file is not None:
    if st.button("Upload and Process Document"):
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        response = requests.post(
            f"{API_URL}/upload-document",
            files=files
        )

        st.json(response.json())

st.subheader("Ask a Question About the Document")

question = st.text_input(
    "Ask a question",
    placeholder="What are the main risks in this document?"
)

if st.button("Ask AI"):
    response = requests.post(
        f"{API_URL}/ask",
        json={"question": question}
    )

    data = response.json()

    st.subheader("Raw Backend Response")
    st.json(data)

    st.subheader("AI Response")
    st.write(data.get("answer", "No answer returned."))