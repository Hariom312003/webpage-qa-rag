# Webpage Q&A using RAG and Ollama

This project is a Chrome Extension that allows users to ask questions about any webpage using Retrieval-Augmented Generation (RAG) with a local LLM (LLaMA-3 via Ollama).

## Tech Stack
- FastAPI (Backend)
- LangChain + ChromaDB (RAG)
- Ollama (LLaMA-3)
- Chrome Extension (Manifest V3)

## How it works
1. User opens a webpage
2. Chrome extension extracts page content
3. Backend chunks and embeds text
4. ChromaDB stores vectors
5. Ollama generates grounded answers

## Author
Hariom Gupta
