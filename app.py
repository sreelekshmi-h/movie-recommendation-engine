import chromadb
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer


app = FastAPI(title="Movie Recommendation API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("movies")


class SearchRequest(BaseModel):
    query: str
    n_results: int = 5


@app.get("/")
def home():
    return {"message": "API is successfully running"}


@app.post("/search")
def search_movies(request: SearchRequest):
    query_embedding = model.encode(request.query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=request.n_results
    )
    movies = []

    for metadata, document in zip(
        results["metadatas"][0],
        results["documents"][0]
    ):

        movies.append({
            "title": metadata["title"],
            "year": metadata["year"],
            "rating": metadata["rating"],
            "poster": metadata["poster"],
            "overview": document
        })

    return movies