import chromadb
from sentence_transformers import SentenceTransformer
from tmdb import get_popular_movies

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="movies"
)

total_movies = 0
for page in range(1, 11):
    print(f"Fetching page {page}...")

    movies = get_popular_movies(page)

    for movie in movies:
        if not movie.get("overview"):
            continue
        movie_id = str(movie["id"])
        title = movie["title"]
        overview = movie["overview"]
        year = movie.get("release_date", "")[:4]
        rating = movie.get("vote_average", 0)
        poster = ""
        if movie.get("poster_path"):
            poster = (
                "https://image.tmdb.org/t/p/w500"
                + movie["poster_path"]
            )
        embedding = model.encode(overview).tolist()
        collection.add(
            ids=[movie_id],
            embeddings=[embedding],
            documents=[overview],
            metadatas=[{
                "title": title,
                "year": year,
                "rating": rating,
                "poster": poster
            }]
        )
        total_movies += 1
print(f"\nStored {total_movies} movies successfully!")