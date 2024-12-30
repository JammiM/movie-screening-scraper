"""Module to scrape a url endpoint."""

import os
import logging
import requests
import bs4 as bs
from bs4 import Tag

from dotenv import load_dotenv
load_dotenv()



logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} - {levelname} - {message}",
                    style="{",datefmt="%Y-%m-%d %H:%M")


all_movies=[]


def retrieve_url_endpoint():
    """Function to retrieve the url endpoint."""
    response_object = requests.get(os.getenv("API_URL"), timeout=10)
    soup = bs.BeautifulSoup(response_object.content, 'html.parser')

    movies_div = soup.select_one('#pills-grid > div')

    return movies_div

def extract_text_from_div(div_content):
    """Function to extracts text from the div."""
    for x in div_content:
        if isinstance(x, Tag):

            title = x.find('div', {"class": "title"}).text
            dates = x.find('div', {"class": "text"}).text
            film_cert = x.find('div', {"class": "film-cert"}).text
            link = x.find('a')['href']
            img = x.find('div', {"role": "img"}).get('style')


            if x.find('div', {"class": "subheading"}) is None:
                subheading = ''
            else:
                subheading = x.find('div', {"class": "subheading"}).text

            movie_properties =[title,film_cert,dates,link,img,subheading]
            all_movies.append(create_single_movie(movie_properties))
    print(all_movies)


def create_single_movie(movie_props):
    """Creates a single movie."""

    movie = {
        "title": movie_props[0],
        "date": movie_props[1],
        "rating": movie_props[2],
        "link": movie_props[3],
        "img": movie_props[4],
        "subheading":movie_props[5]
    }
    return movie
