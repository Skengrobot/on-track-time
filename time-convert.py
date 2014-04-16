#!/usr/bin/python
#
#   Converting time string to something else then doing some stuff
#

import re
import requests
import sys 
from bs4 import BeautifulSoup as bs

def find_events(url):
    # Frame where event list is located
    req = requests.get(url+'evtindex.htm')
    the_page = req.text
    
    soup = bs(the_page)

    # Filter out only urls that are finals
    finals_urls = []
    filt = re.compile(r'F[0-9][0-9][0-9].htm$')
    for link in soup.find_all('a'):
        thisurl = link.get('href')
        if filt.search(thisurl) is not None:
            finals_urls.append(thisurl)

    # Pull all result pages
    for i in range(len(finals_urls)):
        parse_event_page(url+finals_urls[i])


def parse_event_page(event_url):
    req = requests.get(event_url)
    event_page = req.text

    eventsoup = bs(event_page)
    
    filt = re.compile(r'Event [0-9]')
    print eventsoup.b.string
#     for event in eventsoup.find_all('b'):
#         if filt.search(event.contents) is not None:
#             print event


if len(sys.argv) == 1:
    sys.exit("You fucked up")

find_events(sys.argv[1])
