# 🎬 Movie Recommendation Engine
<img width="933" height="356" alt="image" src="https://github.com/user-attachments/assets/58f67e84-aeb7-4807-8aaf-aa592631a3bd" />

<img width="931" height="503" alt="image" src="https://github.com/user-attachments/assets/36a36304-bd22-47d4-9da9-fd64c741ea69" />


## What it does

The **Movie Recommendation Engine** is an AI-powered semantic search application that helps users discover movies using natural language descriptions instead of exact keywords.

Unlike traditional search systems, this application understands the **meaning** behind a user's query by converting both movie descriptions and user queries into vector embeddings using the **all-MiniLM-L6-v2** embedding model. It then performs semantic similarity search with **ChromaDB** to recommend the most relevant movies.

### Example Searches
- "A mind-bending thriller with unexpected plot twists"
- "A space adventure with aliens and futuristic technology"
- "A funny detective movie with mystery"

---

## Tech Stack

- **Backend:** FastAPI
- **Vector Database:** ChromaDB
- **Embedding Model:** all-MiniLM-L6-v2 (Sentence Transformers)
- **Frontend:** HTML, CSS, JavaScript
- **Movie Data Source:** TMDB (The Movie Database) API
- **Language:** Python

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd movie-recommendation-engine
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Add your TMDB API key:

```env
TMDB_API_KEY=your_tmdb_api_key
```

### 5. Ingest movie data

Fetch movie information from TMDB, generate embeddings, and store them in ChromaDB.

```bash
python ingest.py
```

### 6. Start the FastAPI server

```bash
fastapi run app.py
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

### 7. Open the frontend

Open `index.html` in your browser (or serve the frontend using your preferred web server).

---

## Environment Variables

Create a `.env` file in the project root.

```env
TMDB_API_KEY=your_tmdb_api_key
```

---

## Features

- 🔍 Semantic movie search using natural language
- 🎬 Live movie data fetched from TMDB
- 🧠 AI-powered recommendations using sentence embeddings
- ⚡ Fast similarity search with ChromaDB
- 🎨 Modern, responsive user interface
- 📄 Displays movie posters, ratings, release year, and overview

---

## Example Query

**Input**

> "A mind-bending thriller with unexpected plot twists"

**Output**

- Inception
- Shutter Island
- The Prestige
- Gone Girl
- Knives Out

