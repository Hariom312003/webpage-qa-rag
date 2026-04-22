# 🌐 Webpage Q&A using RAG + Local LLM (Ollama)

A full-stack AI system that enables users to **ask natural language questions about any webpage** using a Chrome Extension powered by **Retrieval-Augmented Generation (RAG)** and a **local LLM (LLaMA 3 via Ollama)**.

⚡ No paid APIs  
🔒 Privacy-friendly (fully local)  
🧠 Answers grounded strictly in webpage content  

---

## 🚀 Key Features

- 🔍 Ask questions about any webpage in real time  
- 🧠 Retrieval-Augmented Generation (RAG) architecture  
- 💻 Fully local LLM using Ollama (LLaMA 3)  
- ⚡ Chrome Extension (Manifest V3)  
- 🧩 Efficient text chunking and semantic search  
- 🛡️ Answers grounded strictly in webpage content  

---

## 🧠 Why This Project?

Traditional LLMs often:
- ❌ Hallucinate answers  
- ❌ Use external/unverified knowledge  
- ❌ Require paid APIs  

### ✅ Solution

This project uses **RAG** to ensure:
- Answers come only from webpage data  
- Transparent and explainable responses  
- No dependency on paid APIs  
- Fully offline and privacy-friendly setup  

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
Ollama (LLaMA 3)
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
8. Prompt + context sent to LLaMA 3  
9. Grounded answer returned  

---

## 🧰 Tech Stack

### 🔹 Backend
- FastAPI  
- LangChain  
- ChromaDB  
- Ollama (LLaMA 3)  

### 🔹 Frontend
- Chrome Extension (Manifest V3)  
- HTML, CSS, JavaScript  

### 🔹 AI / ML
- Retrieval-Augmented Generation (RAG)  
- Local Embeddings + LLM  

---

## 📁 Project Structure
webpage-qa-rag/
│
├── backend/
│ ├── app.py
│ ├── rag_pipeline.py
│ ├── vector_store.py
│ └── requirements.txt
│
├── chrome-extension/
│ ├── manifest.json
│ ├── content.js
│ ├── popup.html
│ ├── popup.js
│ └── background.js
│
├── .gitignore
└── README.md

---

## ⚙️ Setup Instructions (Linux)

### 1️⃣ Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3
ollama serve

2️⃣ Backend Setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn app:app --reload --port 8001
📍 Backend runs at:- http://127.0.0.1:8001/

3️⃣ Load Chrome Extension
1.Open Chrome → chrome://extensions/
2.Enable Developer Mode
3.Click Load Unpacked
4.Select chrome-extension/ folder

🧪 How to Use
1.Open any webpage
2.Click the extension icon
3.Click Scan Page
4.Ask questions like:
  *"What is this page about?"
  *"What are the main features?"
5.Get accurate answers based only on page content

🔐 Design Decisions
-❌ No cloud APIs → avoids cost & privacy issues
-✅ Local LLM → offline capability
-✅ RAG → reduces hallucinations
-✅ ChromaDB → fast similarity search
-✅ Chrome Extension → seamless user experience

🚀 Future Improvements
-🔄 Streaming responses
-📌 Answer source highlighting
-🧠 Multi-page memory
-🔁 Automatic page re-scan
-🎯 Section-wise semantic search
-🎨 UI improvements

👨‍💻 Author
-Hariom Gupta
