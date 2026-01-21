from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer
import pinecone
import requests

app = Flask(__name__)

# ---------- Pinecone Setup ----------
pinecone.init(
    api_key="YOUR_PINECONE_API_KEY",
    environment="us-east-1"
)

index = pinecone.Index("jarvis-index")

# ---------- Embedding Model ----------
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------- Sample Knowledge ----------
documents = [
    "Board members need quick insights into governance and risk.",
    "Compliance reports are generated quarterly for audit purposes.",
    "AI can summarize large governance datasets efficiently."
]

# ---------- Upsert (run once) ----------
for i, doc in enumerate(documents):
    embedding = embed_model.encode(doc).tolist()
    index.upsert([(str(i), embedding, {"text": doc})])

# ---------- Routes ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json["message"]

    query_vector = embed_model.encode(user_query).tolist()

    result = index.query(
        vector=query_vector,
        top_k=1,
        include_metadata=True
    )

    context = result["matches"][0]["metadata"]["text"]

    # Call self-hosted LLaMA via Ollama
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Context: {context}\nQuestion: {user_query}"
        }
    )

    answer = response.json()["response"]
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
