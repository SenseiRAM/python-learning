from typing import List

from requests import get
from collections import namedtuple

Result = namedtuple('Result', 'category, id, url, '
                              'title, description'
                    )


def talk_python_search(keyword: str) -> List[Result]:
    url = f'https://search.talkpython.fm/api/search?q={keyword}'

    resp = get(url)
    resp.raise_for_status()

    results = resp.json()
    response = []
    for r in results.get('results'):
        if r['category'] == 'Episode':
            response.append(Result(**r))
    return response
