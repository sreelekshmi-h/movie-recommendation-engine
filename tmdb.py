import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("TMDB_API_KEY")
url = f"https://api.themoviedb.org/3/movie/popular"

def get_popular_movies(page=1):
    params = {
        "api_key": api_key,
        "language": "en-US",
        "page": page
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()["results"]
    else:
        print("Error:", response.status_code)
        print(response.text)
        return []

if __name__=="__main__":
    movies=get_popular_movies()
    print(f"Fetched {len(movies)} movies:\n")
    for movie in movies:
        print(f"Title: {movie['title']}")
        print(f"Release Date:{movie.get('release_date')}")
        print(f"Rating:{movie.get('vote_average')}")
        print(f"Overview:{movie['overview'][:100]}...")
        print("-"*60)