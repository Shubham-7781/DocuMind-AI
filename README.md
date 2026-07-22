# 📚 DocuMind AI — Chat with Multiple PDFs using RAG

**DocuMind AI** is a Retrieval-Augmented Generation (RAG) chatbot that lets you upload multiple PDF documents and have a natural, conversational Q&A session with them. Instead of manually searching through pages of text, just ask a question in plain English and get an accurate, context-aware answer — grounded in your own documents.

Built with **LangChain**, **FAISS**, **HuggingFace Sentence Transformers**, and **OpenAI GPT**, wrapped in a simple **Streamlit** UI.

---

## ✨ Features

- 📄 **Multi-PDF upload** — ask questions across several documents at once, not just one
- 💬 **Conversational memory** — follow-up questions are automatically rephrased into standalone questions using prior chat context, so you can have a natural back-and-forth instead of repeating yourself
- 🔍 **Semantic search, not keyword search** — retrieves the most *relevant* chunks of text using vector embeddings, even if your question doesn't use the exact same words as the document
- 🧠 **Local embeddings** — uses the `all-MiniLM-L6-v2` sentence-transformer model (runs on CPU, no API cost for embedding)
- ⚡ **Fast, in-memory vector store** — powered by FAISS for efficient similarity search
- 🖥️ **Simple chat UI** — clean, styled chat interface built entirely in Streamlit

---

## 🧩 How It Works (RAG Pipeline)

```
 PDF Upload
     │
     ▼
Text Extraction (PyPDF2)
     │
     ▼
Chunking (LangChain CharacterTextSplitter)
     │
     ▼
Embedding (HuggingFace all-MiniLM-L6-v2)
     │
     ▼
Vector Store (FAISS)
     │
     ▼
User Question ──► Standalone Question Rephrasing (Custom Prompt + Chat History)
     │
     ▼
Similarity Search (Top-k relevant chunks retrieved)
     │
     ▼
Answer Generation (OpenAI ChatGPT via ConversationalRetrievalChain)
     │
     ▼
Response shown in Chat UI (with conversation memory)
```

1. **Extract** — Text is pulled out of every uploaded PDF page-by-page using `PyPDF2`.
2. **Chunk** — The combined text is split into overlapping ~1000-character chunks (`CharacterTextSplitter`) so context isn't lost at chunk boundaries.
3. **Embed** — Each chunk is converted into a vector using the `all-MiniLM-L6-v2` sentence-transformer model, run locally on CPU.
4. **Store** — Vectors are indexed in a **FAISS** in-memory vector store for fast similarity search.
5. **Retrieve** — When you ask a question, LangChain's `ConversationalRetrievalChain` first rephrases it into a standalone question (using a custom prompt + chat history), then retrieves the most relevant chunks from FAISS.
6. **Generate** — The retrieved context + your question are passed to OpenAI's GPT model, which generates a grounded answer.
7. **Remember** — `ConversationBufferMemory` keeps track of the full conversation so follow-up questions stay coherent.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangChain |
| PDF Parsing | PyPDF2 |
| Embeddings | HuggingFace `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Store | FAISS |
| LLM | OpenAI GPT (via `ChatOpenAI`) |
| Memory | LangChain `ConversationBufferMemory` |
| Config | python-dotenv |

---

## 📁 Project Structure

```
DocuMind-AI/
├── app.py               # Main Streamlit application & RAG pipeline
├── htmlTemplates.py      # Chat UI styling (CSS + HTML templates for user/bot bubbles)
├── requirements.txt      # Python dependencies
├── .env                  # API keys (not committed — see setup below)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- An [OpenAI API key](https://platform.openai.com/api-keys)

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
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your-openai-api-key-here
```

### 5. Run the app
```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501** (Streamlit's default port).

---

## 💡 Usage

1. Open the app in your browser.
2. In the sidebar, upload one or more PDF files.
3. Click **"Process"** — this extracts text, chunks it, generates embeddings, and builds the vector store.
4. Type your question in the input box and hit enter.
5. Ask follow-up questions naturally — DocuMind AI remembers the conversation context.

---

## 🎯 Why This Project (Final Year Relevance)

This project demonstrates a complete, modern **RAG pipeline** end-to-end:
- Document ingestion & preprocessing
- Text chunking strategy and its trade-offs
- Embedding generation and vector similarity search
- Prompt engineering for conversational question rephrasing
- LLM-based answer generation grounded in retrieved context
- Conversational memory management

These are core concepts in applied NLP / LLM engineering, making it a strong technical talking point in interviews and vivas — while also being a genuinely useful tool (research, legal docs, study notes, etc.).

---

## 🔮 Possible Improvements / Roadmap

Ideas to extend this project further for a stronger submission:

- [ ] **Per-document source attribution** — show which PDF and page an answer came from
- [ ] **Persistent vector store** — save embeddings to disk (or Supabase/Pinecone) instead of recomputing on every session
- [ ] **Streaming responses** — stream tokens as they're generated instead of waiting for the full answer
- [ ] **Evaluation metrics** — measure retrieval precision/recall on a labeled Q&A set for your final report
- [ ] **Support for other file types** — DOCX, TXT, or scanned/OCR PDFs
- [ ] **Deploy to Streamlit Community Cloud** for a live demo link.
