
# 🌐 Webpage Q&A using RAG and Ollama

A full-stack AI project that enables users to ask natural language questions
about **any open webpage** using a **Chrome Extension** powered by
**Retrieval-Augmented Generation (RAG)** and a **local LLM (LLaMA-3 via Ollama)**.

This system generates **accurate, hallucination-free answers** strictly based
on the webpage content — without using any paid cloud APIs.

---

## 🚀 Key Features

- 🔍 Ask questions about any webpage in real time
- 🧠 Retrieval-Augmented Generation (RAG) architecture
- 💻 Fully local LLM using Ollama (LLaMA-3)
- ⚡ Chrome Extension (Manifest V3)
- 🧩 Efficient text chunking and semantic search
- 🛡️ Answers grounded strictly in webpage content

---

## 🧠 Why This Project?

Traditional LLMs often hallucinate or use external knowledge.
This project solves that problem using **RAG**, ensuring:

- Answers come only from webpage data
- Transparent and explainable responses
- No dependency on OpenAI or paid APIs
- Privacy-friendly, offline-capable setup

---

## 🏗️ System Architecture

Webpage  
↓  
Chrome Extension (DOM Extraction)  
↓  
FastAPI Backend  
↓  
Text Cleaning & Chunking  
↓  
Embedding Generation  
↓  
ChromaDB (Vector Store)  
↓  
Relevant Context Retrieval  
↓  
Ollama (LLaMA-3)  
↓  
Answer to User

---

## 🔄 End-to-End Pipeline

1. User opens any webpage
2. Chrome Extension extracts visible text
3. User clicks **Scan Page**
4. Backend:
   - Cleans and chunks text
   - Converts chunks into embeddings
5. ChromaDB stores vectors
6. User asks a question
7. Backend retrieves relevant chunks
8. Prompt + context sent to LLaMA-3 (Ollama)
9. Grounded answer returned to extension

---

## 🧰 Tech Stack

### Backend
- FastAPI
- LangChain
- ChromaDB
- Ollama (LLaMA-3)

### Frontend
- Chrome Extension (Manifest V3)
- HTML, CSS, JavaScript

### AI / ML
- Retrieval-Augmented Generation (RAG)
- Local Embeddings + LLM

---

## 📁 Project Structure

webpage-qa-rag/
├── backend/
│ ├── app.py
│ ├── rag_pipeline.py
│ ├── vector_store.py
│ ├── requirements.txt
│
├── chrome-extension/
│ ├── manifest.json
│ ├── content.js
│ ├── popup.html
│ ├── popup.js
│ ├── background.js
>>>>>>> 19a09a1 (Improve README with detailed architecture, pipeline, and setup)
│
├── .gitignore
├── README.md

<<<<<<< HEAD

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
=======
---

## ⚙️ Setup Instructions (Linux)

### 1️⃣ Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3
ollama serve

2️⃣ Backend Setup:-
 cd backend
 python3 -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt
 uvicorn app:app --reload --port 8001

Backend runs at:-
  http://127.0.0.1:8001

3️⃣ Load Chrome Extension:-

1.Open Chrome → chrome://extensions

2.Enable Developer Mode
>>>>>>> 19a09a1 (Improve README with detailed architecture, pipeline, and setup)

3.Click Load unpacked

4.Select chrome-extension/ folder

🧪 How to Use

1.Open any webpage

2.Click the extension icon

3.Click Scan Page

<<<<<<< HEAD
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
=======
4.Ask questions like:

  "What is this page about?"

  "What are the main features?"

5.Get accurate, page-grounded answers

🔐 Design Decisions:-

> Local LLM → No cost, privacy-friendly

> RAG architecture → Prevent hallucinations

> ChromaDB → Fast vector search

> Chrome Extension → Seamless UX

🚀 Future Enhancements:-

> Streaming responses

> Highlight answer source text

> Multi-page memory

> Automatic page re-scan

> UI improvements

👨‍💻 Author
>>>>>>> 19a09a1 (Improve README with detailed architecture, pipeline, and setup)

Hariom Gupta
