'''
A script that imports data from program/job applicants and factors most common
data points. As is, it figures out the most common city from which people
are applying. A more robust version would allow the user to choose which stats
to count, or even count them all and prepare a report.

TODO parse the specific dates out of the submission dates, so the user could
easily find the most common submission date. Other ideas: Spit the results into
a totally new CSV report, add a GUI, etc.

This script was created as part of 100 Days of Code, and aimed specifically
at learning how to work with default dictionaries and named tuples.
'''
from collections import defaultdict, namedtuple, Counter, deque
import csv
from datetime import datetime

# Essentially using a namedtuple as a class with no methods
Applicant = namedtuple('Applicant', 'city company_name employment_status submit_date')

# Location of data (your location may differ)
applicant_data = 'applicant_dataset.csv'


# Create a defaultdict of states as keys
# and a list namedtuples as values
def get_location_data(data):
    locations = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):

            try:
                city = line['city']
                state = line['state']
                company_name = line['company_name']
                employment_status = line['employment_status']
                submit_date = line['submit_date']
            except ValueError:
                raise
                continue

            a = Applicant(city=city,
                          company_name=company_name,
                          employment_status=employment_status,
                          submit_date=submit_date
                          )

            locations[state].append(a)
    return locations


def main():
    locations = get_location_data(applicant_data)
    # Empty list to compile data
    cities = []

    # Add each instance of a city to the list
    # These three lines of code took me over an hour to figure out :\
    for state in locations:
        for i, item in enumerate(locations[state]):
            cities.append(locations[state][i].city)

    # Tally the most common cities where applicants are located
    city_count = Counter(cities).most_common(10)

    print(city_count)

    done = input('Complete, press enter to quit. ')


if __name__ == '__main__':
    main()
