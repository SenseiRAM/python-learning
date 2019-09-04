import csv
import urllib
from urllib.parse import quote
import datetime
from dateutil.parser import parse
import pytz

# If you need to change your working directory.
#import os
#os.chdir('C:\\WORKING_DIRECTORY')

event_file = ('gcal_link_info.csv')
gcal_file = ('gcal_links.csv')
events = []
gcal_links = []
gcal_csv_list = []

central_timezone = pytz.timezone('America/Chicago')
utc_timezone = pytz.timezone('Etc/UTC')

class Event():

    def __init__(self, event, desc, start_time, end_time, location, gcal_str):

        self.event = event
        self.desc = desc
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.gcal_str = gcal_str

with open(event_file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    for event in rd:
        events.append(Event(**event))

for i in range(len(events)):
    start_date_str = events[i].start_time
    end_date_str = events[i].end_time
    start_time_obj = parse(start_date_str).astimezone(central_timezone)
    start_time_obj = start_time_obj.astimezone(utc_timezone)
    end_time_obj = parse(end_date_str).astimezone(central_timezone)
    end_time_obj = end_time_obj.astimezone(utc_timezone)

    gcal_date_string = start_time_obj.strftime('%Y%m%d') + 'T' + start_time_obj.strftime('%H%M%S') + 'Z%2F' + end_time_obj.strftime('%Y%m%d') + 'T' + end_time_obj.strftime('%H%M%S') + 'Z'

    newstring = 'http://www.google.com/calendar/event?action=TEMPLATE&dates=' + gcal_date_string + '&text=' + quote(events[i].event) + '&location=' + quote(events[i].location) + '&details=' + quote(events[i].desc)

    events[i].gcal_str = newstring

for event in events:
    gcal_csv_list.append([event.event, event.gcal_str])

with open(gcal_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for event in gcal_csv_list:
        writer.writerow(event)
