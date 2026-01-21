Diligent Jarvis – Enterprise AI Assistant

Problem Statement
Design and implement a personal AI assistant for enterprise users using:
- a **self-hosted Large Language Model (LLM)**,
- a **vector database (Pinecone)**,
- and a **conversational chatbot interface**,

that can understand natural language queries and return contextual, relevant responses.



Solution Overview
Diligent Jarvis is a lightweight enterprise AI assistant inspired by “Jarvis”.  
It follows a **Retrieval-Augmented Generation (RAG)** approach:

1. User asks a question through a chatbot UI  
2. The query is converted into vector embeddings  
3. Relevant context is retrieved from **Pinecone**  
4. The retrieved context is passed to a **self-hosted LLM (via Ollama)**  
5. The model generates a contextual response  



Architecture

User  
↓  
Chatbot UI (HTML + JS)  
↓  
Flask Backend (Python)  
↓  
Embedding Model (384-dim)  
↓  
Pinecone Vector Database (`jarvis-index`)  
↓  
Relevant Context  
↓  
Self-hosted LLM (Ollama)  
↓  
Response to User  



⚙️ Tech Stack

| Component | Technology |
|---------|------------|
| Backend | Flask (Python) |
| Vector DB | Pinecone |
| Embeddings | Sentence Transformers (384-dim) |
| LLM | Self-hosted via Ollama |
| UI | HTML + JavaScript |
| Cloud | AWS (Pinecone us-east-1) |



 🔑 Key Features
- Natural language query understanding
- Semantic search using Pinecone
- Context-aware AI responses
- Lightweight, minimal chatbot UI
- Enterprise-ready RAG architecture

---

📊 Success Metrics
- Response relevance
- Retrieval accuracy
- Latency
- User experience



⚠️ Risks & Limitations
- Limited demo knowledge base
- Possible LLM hallucinations
- Local LLM depends on system resources



## 🚀 Future Enhancements
- Larger enterprise knowledge base
- Authentication & role-based access
- Better prompt engineering
- Cloud deployment



## ▶️ How to Run

1. Start Ollama:
```bash
ollama run gemma3:4b

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set Pinecone API Key (Windows)
setx PINECONE_API_KEY "your_pinecone_api_key_here"


Restart terminal after setting the variable.

4️⃣ Run the backend
python app.py

5️⃣ Open in browser
http://127.0.0.1:5000

📂 Repository Structure
diligent-jarvis/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html