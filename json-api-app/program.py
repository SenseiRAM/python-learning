import api

# TODO Turn this app into a basic api skeleton. Should be a framework for any search API.
def main():
    keyword = input('Please enter a title search term: ')
    results = api.find_movie_by_title(keyword)
    print(f'There are {len(results)} movie(s) found.')
    for r in results:
        print(f"Title: {r.title} with score of {r.imdb_score}")


if __name__ == '__main__':
    main()