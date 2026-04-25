
import streamlit as st
import os
from utils import summarizer


def main():
    st.set_page_config(page_title="PDF Summarizer")
    st.title("PDF Summarizing App")
    st.write("Summarize your PDF files within seconds")
    st.divider()

    pdf = st.file_uploader("Upload your PDF document", type="pdf")
    button = st.button("Generate Summary")

    # ⚠️ NEVER hardcode API keys in real apps
    os.environ["GOOGLE_API_KEY"] = "AIzaSyCgGov-XjaSx6xN4pS73QBxvPcd9VAWdBM"

    if pdf is not None and button:

        with st.spinner("Generating summary..."):
            response = summarizer(pdf)

        st.subheader("Summary of file")
        st.write(response)


if __name__ == "__main__":
    main()    