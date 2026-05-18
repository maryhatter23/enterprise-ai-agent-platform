import streamlit as st
import requests

st.set_page_config(page_title="Enterprise AI Agent Platform")

st.title("Enterprise AI Agent Platform")

st.write(
    "Production-style multi-agent AI workflow platform."
)

st.subheader("Ask Backend")

question = st.text_input(
    "Question",
    placeholder="What are the payment terms?"
)

if st.button("Send Request"):
    try:
        response = requests.get("http://127.0.0.1:8000/")
        st.success(response.json())
    except Exception as e:
        st.error(str(e))