🌐 Webpage Q&A using RAG and Ollama:-

A Chrome Extension + Backend AI system that allows users to ask natural language questions about any open webpage.
The system uses Retrieval-Augmented Generation (RAG) with a local Large Language Model (LLaMA-3 via Ollama) to generate grounded, hallucination-free answers strictly from webpage content.

This project works fully offline (local LLM) and does not rely on paid APIs.

🚀 Key Features:-

-> 🔍 Ask questions about any webpage in real time

-> 🧠 Uses RAG (Retrieval-Augmented Generation) for accurate answers

-> 💻 Runs locally using Ollama (LLaMA-3) — no OpenAI key required

-> ⚡ Chrome Extension with clean UI (Manifest V3)

-> 🧩 Efficient text chunking and vector search

-> 🛡️ Answers are strictly grounded in webpage content

🧠 Why RAG?

Traditional LLMs can hallucinate or use external knowledge.

# RAG fixes this by:

 1.Extracting content from the webpage

 2.Converting it into embeddings

 3.Retrieving only relevant chunks

 4.Sending retrieved context to the LLM

➡️ Result: accurate, explainable, context-aware answers

🏗️ System Architecture:-
┌───────────────┐
│  Web Browser  │
│ (Any Webpage) │
└───────┬───────┘
        │
        ▼
┌────────────────────┐
│ Chrome Extension   │
│ - content.js       │
│ - popup.js         │
│ - background.js    │
└───────┬────────────┘
        │  (Extracted Text)
        ▼
┌────────────────────┐
│ FastAPI Backend    │
│ - /scan endpoint   │
│ - /ask endpoint    │
└───────┬────────────┘
        │
        ▼
┌────────────────────────────┐
│ RAG Pipeline (LangChain)   │
│ - Text Cleaning            │
│ - Chunking                 │
│ - Embeddings               │
│ - Retrieval                │
└───────┬────────────────────┘
        │
        ▼
┌────────────────────┐
│ ChromaDB           │
│ (Vector Store)     │
└───────┬────────────┘
        │ (Top-K Chunks)
        ▼
┌────────────────────┐
│ Ollama (LLaMA-3)   │
│ Local LLM          │
└────────────────────┘

🔄 Complete Pipeline (Step-by-Step)

1:User opens any webpage

2:Chrome Extension extracts visible DOM text

3:User clicks “Scan Page”

4:Backend:-

  1->Cleans text
  
  2->Splits into chunks

  3->Generates embeddings

5:Embeddings are stored in ChromaDB

6:User asks a question

7:Backend:-

   1->Embeds the question

   2->Retrieves relevant chunks

   3->Builds a prompt with context

8:Ollama (LLaMA-3) generates a grounded answer

9:Answer is shown in the extension UI

🧰 Tech Stack
Backend:-

  1.FastAPI

  2.LangChain

  3.ChromaDB

  4.Ollama (LLaMA-3)

Frontend:-

  1.Chrome Extension (Manifest V3)

  2.HTML, CSS, JavaScript

ML / AI:-

  1.Retrieval-Augmented Generation (RAG)

  2.Local embeddings + LLM

📁 Project Structure:-
  webpage-qa-rag/
│
├── backend/
│   ├── app.py              # FastAPI server
│   ├── rag_pipeline.py     # RAG logic
│   ├── vector_store.py     # ChromaDB integration
│   ├── requirements.txt
│
├── chrome-extension/
│   ├── manifest.json
│   ├── content.js          # Extract webpage text
│   ├── popup.html
│   ├── popup.js            # UI logic
│   ├── background.js
│
├── .gitignore
├── README.md


⚙️ Setup Instructions (Linux):-
 1️⃣ Install Ollama:-
      curl -fsSL https://ollama.com/install.sh | sh
    Pull the model:-
      ollama pull llama3
    Run Ollama:-
      ollama serve
2️⃣ Backend Setup:-
      cd backend
      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
    Run server:-
      uvicorn app:app --reload --port 8001
    Backend runs at:-
       http://127.0.0.1:8001

3️⃣ Load Chrome Extension

1.Open Chrome → chrome://extensions

2.Enable Developer mode

3.Click Load unpacked

4.Select chrome-extension/ folder

🧪 How to Use

1.Open any webpage

2.Click the extension icon

3.Click Scan Page

4.Ask a question like:

  “What is this page about?”

  “What are the main features?”

5.Get an accurate answer from page content only

🔐 Design Decisions

->❌ No cloud APIs → avoids cost & privacy issues

->✅ Local LLM → faster iteration, offline support

->✅ RAG → prevents hallucinations

->✅ ChromaDB → fast similarity search

🚀 Future Improvements

-> Streaming responses

-> Multi-page memory

-> Page re-scan auto detection

-> Answer citations (highlight source text)

-> Semantic section-wise search

👨‍💻 Author:-

Hariom Gupta
