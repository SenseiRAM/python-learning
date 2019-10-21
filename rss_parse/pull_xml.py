import requests

URL = "https://www.metacritic.com/rss/games/switch.xml"

if __name__ == '__main__':
    r = requests.get(URL)
    with open('metacritic_switch.xml', 'wb') as f:
        f.write(r.content)