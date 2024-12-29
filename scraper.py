"""Module to scrape a url endpoint."""

import os
import logging
import requests
import bs4 as bs

from dotenv import load_dotenv
load_dotenv()



logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} - {levelname} - {message}",
                    style="{",datefmt="%Y-%m-%d %H:%M")


all_titles=[]

def retrieve_url_endpoint():
    """Function to retrieve the url endpoint."""
    response_object = requests.get(os.getenv("API_URL"), timeout=10)
    soup = bs.BeautifulSoup(response_object.content, 'html.parser')

    movies_div = soup.select('#pills-grid > div')

    for x in movies_div:


        titles = x.find_all("div", {"class": "title"})
        # film-cert
        # subheading
        # text
        for single_title in titles:
            all_titles.append(single_title.text)

    print(all_titles)
