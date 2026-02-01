from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from vector_store import retrieve_documents
from langchain_ollama import OllamaLLM

def prepare_documents(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    documents = [
        Document(page_content=chunk) for chunk in chunks
    ]

    return documents

def generate_answer(question: str):
    docs = retrieve_documents(question, k=3)

    if not docs:
        return "No relevant information found. Please scan the page first."

    context = "\n\n".join([doc.page_content for doc in docs])

    llm = OllamaLLM(model="llama3")

    prompt = f"""
You are an assistant that answers strictly using the given context.

Context:
{context}

Question:
{question}

Answer:
"""

    return llm.invoke(prompt)

