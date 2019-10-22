from movie_search_client import MovieSearchClient


def main():
    val = 'RUN'

    while val:
        print('Welcome to Movie Search!')
        val = input('Would you like to search by [k]eyword or [d]irector? (or [q]uit? ').lower()

        if val == 'k':
            search_by_keyword()
        elif val == 'd':
            search_by_director()
        elif val == 'q':
            val = None


def search_by_keyword():
    keyword = input('Please enter a keyword to search for: ').lower()

    svc = MovieSearchClient()
    response = svc.movies_by_keyword(keyword)
    response.raise_for_status()
    movies = response.json()['hits']

    for idx, m in enumerate(movies, 1):
        print(f"{idx}. {m.get('title')}")

    if not movies:
        print('No results found...')

    print()


def search_by_director():
    director = input("Please enter a director's last name to search for: ").lower()

    svc = MovieSearchClient()
    response = svc.movies_by_director(director)
    response.raise_for_status()
    movies = response.json()['hits']

    for idx, m in enumerate(movies, 1):
        print(f"{idx}. {m.get('title')}")

    if not movies:
        print('No results found...')

    print()


if __name__ == '__main__':
    main()