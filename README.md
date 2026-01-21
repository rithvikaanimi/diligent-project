# Diligent Jarvis – Enterprise AI Assistant

Problem Statement
Design and implement a personal AI assistant for enterprise users using:
- a **self-hosted Large Language Model (LLM)**,
- a **vector database (Pinecone)**,
- and a **conversational chatbot interface**,

that can understand natural language queries and return contextual, relevant responses.

---

Solution Overview
Diligent Jarvis is a lightweight enterprise AI assistant inspired by “Jarvis”.  
It follows a **Retrieval-Augmented Generation (RAG)** approach:

1. User asks a question through a chatbot UI  
2. The query is converted into vector embeddings  
3. Relevant context is retrieved from **Pinecone**  
4. The retrieved context is passed to a **self-hosted LLaMA model (via Ollama)**  
5. The model generates a contextual response for the user  

This approach ensures accurate, explainable, and enterprise-ready AI responses.

---

Architecture

User
↓
Chatbot UI (HTML + JS)
↓
Flask Backend (Python)
↓
Embedding Model (384-dim)
↓
Pinecone Vector Database (jarvis-index)
↓
Relevant Context
↓
Self-hosted LLaMA (Ollama)
↓
Response to User

yaml
Copy code

---

## ⚙️ Tech Stack

| Component | Technology |
|--------|-----------|
Backend | Flask (Python) |
Vector Database | Pinecone |
Embeddings | Sentence Transformers (384 dimensions) |
LLM | LLaMA (self-hosted using Ollama) |
UI | HTML + JavaScript |
Cloud | AWS (Pinecone us-east-1) |

---

## 🔑 Key Features
- Natural language query understanding
- Semantic search using Pinecone vector database
- Context-aware responses using a self-hosted LLM
- Simple and interactive chatbot interface
- Modular and scalable enterprise AI architecture

---

## 🤖 AI / Technical Approach

### Embeddings
- User queries and documents are converted into **384-dimensional vectors**
- Compatible with Pinecone index configuration

### Vector Search
- Pinecone performs **cosine similarity search**
- Retrieves the most relevant enterprise knowledge context

### Self-hosted LLM
- LLaMA is run **locally using Ollama**
- Ensures data privacy and enterprise compliance
- Retrieved context is injected into the prompt for accurate responses

---

📊 Success Metrics
- Relevance of responses
- Retrieval accuracy from Pinecone
- Response latency
- User satisfaction with chatbot answers

---

 Risks & Limitations
- Limited knowledge base for demonstration purposes
- Potential LLM hallucinations
- Local LLM performance depends on system resources

---

Future Enhancements
- Expand enterprise knowledge base
- Add authentication and role-based access
- Improve prompt engineering for higher accuracy
- Deploy backend and LLM using cloud infrastructure

---
▶️ How to Run the Project

1️⃣ Start the self-hosted LLM
```bash
ollama run llama3
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the backend
bash
Copy code
python app.py
4️⃣ Open in browser
cpp
Copy code
http://127.0.0.1:5000
📂 Repository Structure
markdown
Copy code
diligent-jarvis/
│
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
