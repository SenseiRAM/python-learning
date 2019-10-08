import config
import json
import requests
from pprint import pprint

# TODO Create input variables so user can specify search criteria
# "Would you like to search for a [m]ovie, [s]eries, or [e]pisode? " Etc
# API key stored in config.MY_KEY. You'll need to create that yourself.
r = requests.get(f'http://www.omdbapi.com/?s={input("What would you like to search for? ")}&page=1&type=series&apikey={config.MY_KEY}')
data = json.loads(r.text)

# TODO Set up specific parsing functions


def main():
    try:
        if data['Response'] == 'True':
            pprint(data)
    except:
        print("There's been an error of some kind.")


if __name__ == '__main__':
    main()
