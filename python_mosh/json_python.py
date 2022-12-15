import json
from pathlib import Path

movies = [
    {"id": 1, "title": "The Shawshank Redemption", "year": 1994},
    {"id": 2, "title": "The Godfather", "year": 1972},
    {"id": 3, "title": "The Godfather: Part II", "year": 1974},
    {"id": 4, "title": "The Dark Knight", "year": 2008}
]

data = json.dumps(movies)
Path.write_text(Path("movies.json"), data)
