import os
import csv
import collections
import datetime
from typing import List

data = []

Applicant = collections.namedtuple(
    "Applicant",
    "city,"
    "state,"
    "country,"
    "employment_status,"
    "company_name,"
    "submit_date,"
)

def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'applicant_dataset.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        data.clear()
        for row in reader:
            applicant = parse_row(row)
            data.append(applicant)


def parse_row(row):
    # 11/22/2018 10:05pm
    row['submit_date'] = datetime.datetime.strptime(row['submit_date'], '%m/%d/%Y %I:%M%p')
    applicant = Applicant(
        **row
    )

    return applicant


# Possibly have this return a sorted list and manipulate that in the main script instead?
def top_cities(city_num) -> List[Applicant]:
    return list(collections.Counter([x.city for x in data]).most_common(city_num))

# Possibly have this return a sorted list and manipulate that in the main script instead?
def top_companies(company_num):
    return list(collections.Counter([x.company_name for x in data]).most_common(company_num))
