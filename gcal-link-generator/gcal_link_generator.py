import csv
from urllib.parse import quote
from dateutil.parser import parse
import pytz

# If you need to change your working directory.
#import os
#os.chdir('C:\\WORKING_DIRECTORY')

# Simple CSV file to pull info from. This is copied from an Airtable base we use.
event_file = ('gcal_link_info.csv')

# Arbitrary file to write to
gcal_file = ('gcal_links.csv')
events = [] # List of class instances with info about individual events
gcal_links = [] # Gcal template links
gcal_csv_list = [] # Stores data for output csv

# You will want to adjust this to your timezone.
central_timezone = pytz.timezone('America/Chicago')
utc_timezone = pytz.timezone('Etc/UTC')

# TODO Make this a single line namedtuple.
class Event():

    def __init__(self, event, desc, start_time, end_time, location, gcal_str):

        self.event = event
        self.desc = desc
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.gcal_str = gcal_str

# Convert csv to a list of object instances
# The ** operator unpacks the csv row's key, value pairs
# and magically applies them to the Event class' attributes. Amazing!
with open(event_file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    for event in rd:
        events.append(Event(**event))

for i in range(len(events)):
    start_date_str = events[i].start_time
    end_date_str = events[i].end_time

    # Convert all times from your timezone to UTC
    start_time_obj = parse(start_date_str).astimezone(central_timezone)
    start_time_obj = start_time_obj.astimezone(utc_timezone)
    end_time_obj = parse(end_date_str).astimezone(central_timezone)
    end_time_obj = end_time_obj.astimezone(utc_timezone)

    # Create the date portion of the Gcal template URL
    gcal_date_string = start_time_obj.strftime('%Y%m%d') + 'T' + start_time_obj.strftime('%H%M%S') + 'Z%2F' + end_time_obj.strftime('%Y%m%d') + 'T' + end_time_obj.strftime('%H%M%S') + 'Z'

    # Create Gcal template URL
    newstring = 'http://www.google.com/calendar/event?action=TEMPLATE&dates=' + gcal_date_string + '&text=' + quote(events[i].event) + '&location=' + quote(events[i].location) + '&details=' + quote(events[i].desc)

    # Set event's Gcal URL
    events[i].gcal_str = newstring

# Create list for output CSV
for event in events:
    gcal_csv_list.append([event.event, event.gcal_str])

# Create output file
with open(gcal_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for event in gcal_csv_list:
        writer.writerow(event)
