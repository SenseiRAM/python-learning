import feedparser

FEED_FILE = 'metacritic_switch.xml'
feed = feedparser.parse(FEED_FILE)

def list_titles(rss):
    for entry in feed.entries:
        print(f'{entry.published} - {entry.title}')

if __name__ == '__main__':
    list_titles(feed)