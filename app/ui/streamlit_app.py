import streamlit as st
import requests

st.set_page_config(page_title="Enterprise AI Agent Platform")

st.title("Enterprise AI Agent Platform")
st.write("Production-style multi-agent AI workflow platform.")

question = st.text_input(
    "Ask a question",
    placeholder="What are the risks in this contract?"
)

if st.button("Ask AI"):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": question}
        )

        data = response.json()

        st.subheader("Raw Backend Response")
        st.json(data)

        st.subheader("AI Response")
        st.write(data.get("answer", "No answer key returned from backend."))

    except Exception as e:
        st.error(f"Error: {e}")