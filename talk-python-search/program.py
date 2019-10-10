import api
import webbrowser

def main():
    keyword = input('Please enter a search term: ')
    results = api.talk_python_search(keyword)
    browser_direct = ''

    print(f'There are {len(results)} results(s) found.')
    for r in results:
        if r.category == 'Episode':
            print(f"Episode {r.id}: {r.title}\n"
                  f"Description: {r.description[:50]}...\n"
                  f"URL: https://talkpython.fm{r.url}.\n")

    while not isinstance(browser_direct, int):
        try:
            browser_direct = int(input("Please enter the episode number you would like to open. "))
            for r in results:
                if r.id == browser_direct:
                    webbrowser.open(f"https://talkpython.fm{r.url}", new=2)
                    print('Thanks for using the app, and enjoy the show!')
                    return 0
            print('Oops, episode number not in results. Please enter again.')
            browser_direct = ''
        except ValueError:
            print('Please enter a number.')



if __name__ == '__main__':
    main()