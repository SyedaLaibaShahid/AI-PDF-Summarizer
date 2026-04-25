
from pypdf import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI


def summarizer(pdf):
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        if not text.strip():
            return "No readable text found in PDF."

        llm = ChatGoogleGenerativeAI(
            model="models/gemini-2.5-flash",
            temperature=0.3
        )

        prompt = f"""
        Summarize the following PDF content in 3-5 clear sentences:

        {text[:12000]}
        """

        response = llm.invoke(prompt)

        return response.content