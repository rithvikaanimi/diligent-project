from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import requests
import os

app = Flask(__name__)

# -------- Pinecone Setup (NEW SDK + AUTO CREATE INDEX) --------
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

INDEX_NAME = "jarvis-index"

# Create index if it does not exist
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(INDEX_NAME)

# -------- Embedding Model --------
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# -------- Sample Knowledge --------
documents = [
    "Board members need quick insights into governance and risk.",
    "Compliance reports are generated quarterly for audit purposes.",
    "AI can summarize large governance datasets efficiently."
]

# -------- Upsert Knowledge --------
for i, doc in enumerate(documents):
    embedding = embed_model.encode(doc).tolist()
    index.upsert([(str(i), embedding, {"text": doc})])

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

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:4b",
            "prompt": f"Context: {context}\nQuestion: {user_query}"
        }
    )

    answer = response.json()["response"]
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
