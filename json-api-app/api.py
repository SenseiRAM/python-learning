from typing import List

from requests import get
from collections import namedtuple

Movie = namedtuple('Movie', 'imdb_code, title, director, '
                                        'keywords, duration, genres, '
                                        'rating, year, imdb_score')


def find_movie_by_title(keyword: str) -> List[Movie]:
    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'

    resp = get(url)
    resp.raise_for_status()

    results = resp.json()
    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))
    return movies