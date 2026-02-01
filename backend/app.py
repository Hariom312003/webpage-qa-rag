from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from rag_pipeline import prepare_documents, generate_answer
from vector_store import save_documents

app = FastAPI()

# Allow Chrome Extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScanRequest(BaseModel):
    text: str

class AskRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/scan")
def scan_page(data: ScanRequest):
    documents = prepare_documents(data.text)
    saved = save_documents(documents)
    if not saved:
        return {"status": "failed"}
    return {"status": "success"}

@app.post("/ask")
def ask_question(data: AskRequest):
    answer = generate_answer(data.question)
    return {"answer": answer}

