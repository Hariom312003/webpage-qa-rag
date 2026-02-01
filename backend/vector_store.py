from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings

DB_DIR = "./chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def get_vector_store():
    return Chroma(
        persist_directory=DB_DIR,
        embedding_function=embedding_model
    )

def save_documents(documents: list[Document]):
    if not documents:
        return False
    db = get_vector_store()
    db.add_documents(documents)
    db.persist()
    return True

def retrieve_documents(query: str, k: int = 4):
    db = get_vector_store()
    return db.similarity_search(query, k=k)

