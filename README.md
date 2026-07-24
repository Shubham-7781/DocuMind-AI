# 📚 DocuMind AI — Chat with Multiple Documents using RAG

**DocuMind AI** is a Retrieval-Augmented Generation (RAG) chatbot that lets you upload PDF, TXT, or DOCX files and have a natural, conversational Q&A session with them — with every answer traceable back to the exact file and page it came from.

Built with **LangChain**, **FAISS**, **HuggingFace Sentence Transformers**, and **Groq's Llama 3.1** (fast, free-tier LLM inference), wrapped in a polished **Streamlit** UI.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## ✨ Features

- 📄 **Multi-format upload** — PDF, TXT, and DOCX, mixed together in a single session
- 🔗 **Source-cited answers** — every response shows exactly which file(s) and page(s) it was grounded in, ranked and with a text snippet
- 💬 **Conversational memory** — follow-up questions are automatically rephrased into standalone questions using prior chat context
- 🔍 **Semantic search, not keyword search** — retrieves the most *relevant* chunks via vector embeddings, even when your wording doesn't match the document
- 🧠 **Local embeddings** — `all-MiniLM-L6-v2` sentence-transformer runs on CPU, no API cost for embedding
- ⚡ **Fast LLM inference** — powered by [Groq](https://groq.com/) running Llama 3.1 8B
- 📚 **Document library panel** — see every processed file with its chunk count and page count at a glance
- 💡 **Suggested question chips** — one-click prompts to summarize, extract key points, or pull out figures
- 💾 **Persistent vector store** — save a processed index to disk and reload it in a later session instead of re-embedding
- 📥 **Downloadable chat transcript** — export the full conversation as a `.txt` file
- 📊 **Session stats** — file count, chunk count, and processing time shown in the sidebar
- 🧹 **Reliable reset controls** — clearing a conversation properly wipes the chain's memory (not just the display), so old context can never leak into new answers
- 🛡️ **Input validation** — friendly errors for missing API keys, empty uploads, unsupported files, or corrupted documents
- 🎨 **Polished, modern UI** — gradient header, animated chat bubbles, ranked source cards

---

## 🧩 How It Works (RAG Pipeline)

```
 Upload (PDF / TXT / DOCX)
     │
     ▼
Text Extraction (page-aware for PDFs, with per-file metadata)
     │
     ▼
Chunking (LangChain RecursiveCharacterTextSplitter, 1000 chars / 200 overlap)
     │
     ▼
Embedding (HuggingFace all-MiniLM-L6-v2, local CPU inference)
     │
     ▼
Vector Store (FAISS — in-memory, optionally persisted to disk)
     │
     ▼
User Question ──► Standalone Question Rephrasing (Custom Prompt + Chat History)
     │
     ▼
Similarity Search (Top-k relevant chunks retrieved, with source metadata)
     │
     ▼
Answer Generation (Groq Llama 3.1 via ConversationalRetrievalChain)
     │
     ▼
Response + Ranked, Cited Sources shown in Chat UI (with conversation memory)
```

1. **Extract** — Text is pulled from every uploaded file. PDFs are read page-by-page with `PyPDF2` so each chunk keeps a page number; DOCX/TXT keep the filename as their source.
2. **Chunk** — Text is split into overlapping ~1000-character chunks (`RecursiveCharacterTextSplitter`) while preserving source/page metadata on every chunk.
3. **Embed** — Each chunk is converted into a vector with the `all-MiniLM-L6-v2` sentence-transformer model, run locally on CPU (cached across the session for speed).
4. **Store** — Vectors are indexed in a **FAISS** vector store for fast similarity search, with an option to persist the index to disk.
5. **Retrieve** — LangChain's `ConversationalRetrievalChain` first rephrases your question into a standalone question (using chat history), then retrieves the most relevant chunks from FAISS.
6. **Generate** — The retrieved context + question are passed to Groq's Llama 3.1, which generates a grounded answer.
7. **Cite** — The exact source documents used for that answer are shown ranked, with file icon, page number, and snippet, in an expandable panel underneath it.
8. **Remember** — `ConversationBufferMemory` keeps the full conversation coherent across follow-ups, and is properly cleared when you start a new conversation.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangChain |
| Document Parsing | PyPDF2, python-docx |
| Embeddings | HuggingFace `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Store | FAISS (with local persistence) |
| LLM | Groq `llama-3.1-8b-instant` (via `langchain-groq`) |
| Memory | LangChain `ConversationBufferMemory` |
| Config | python-dotenv |

---

## 📁 Project Structure

```
DocuMind-AI/
├── app.py               # Main Streamlit application & RAG pipeline
├── htmlTemplates.py      # Chat UI styling (CSS + HTML templates)
├── requirements.txt      # Python dependencies
├── .env.example           # Template for required environment variables
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A free [Groq API key](https://console.groq.com/keys)

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/DocuMind-AI.git
cd DocuMind-AI
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Copy the template and add your key:
```bash
cp .env.example .env
```
Then edit `.env`:
```
GROQ_API_KEY=your-groq-api-key-here
```
> ⚠️ Never commit your real `.env` file — it's already covered by `.gitignore`.

### 5. Run the app
```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501** (Streamlit's default port).

---

## 💡 Usage

1. Open the app in your browser.
2. In the sidebar, upload one or more PDF / TXT / DOCX files.
3. Click **Process** — this extracts text, chunks it, generates embeddings, and builds the vector store. The sidebar shows a document library plus file/chunk/time stats.
4. Type a question, or click one of the suggested question chips to get started instantly.
5. Expand **"View sources"** under any answer to see exactly which file, page, and text snippet it came from.
6. Ask follow-ups naturally — DocuMind AI remembers the conversation context until you clear it.
7. Optionally **save the index** to disk so you can reload it later without re-processing, or **download the chat transcript** when you're done.

---

## 🎯 Why This Project (Resume / Portfolio Relevance)

This project demonstrates a complete, modern **RAG pipeline** end-to-end:
- Multi-format document ingestion & preprocessing with metadata tracking
- Text chunking strategy and its trade-offs
- Embedding generation and vector similarity search
- Prompt engineering for conversational question rephrasing
- Grounded, source-attributed LLM answer generation
- Conversational memory management, including correct state/session lifecycle handling
- Persistence across sessions via a locally saved FAISS index
- Practical engineering concerns: error handling, input validation, secrets management, UI/UX design

These are core concepts in applied NLP / LLM engineering, making it a strong technical talking point in interviews — while also being a genuinely useful tool (research, legal docs, study notes, etc.).

---

## 🔮 Possible Improvements / Roadmap

- [ ] Token-by-token streaming of answers
- [ ] Multi-user support with per-user saved indexes
- [ ] Evaluation metrics — retrieval precision/recall on a labeled Q&A set
- [ ] OCR support for scanned PDFs
- [ ] Deploy to Streamlit Community Cloud for a live demo link

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
