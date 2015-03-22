#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
from bs4 import BeautifulSoup


def get_title(soup):
    h1 = soup.h1
    span = h1.span
    return span.get_text()


def get_year(soup):
    h1 = soup.h1
    span = h1.find_all("span")
    year_with_brackets = span[1].get_text()
    return year_with_brackets.strip("()")


def get_description(soup):
    p = soup.p
    return p.get_text()


def get_duration(soup):
    i = soup.i
    duration_with_text = i.get_text()
    duration = ""
    for character in duration_with_text:
        if character.isdigit():
            duration += character
    return duration


def get_genre(soup):
    genre = soup.findAll(itemprop="genre")
    return genre[0].get_text()


def get_info(movie_id):
    film_info = {}
    page_content = utils.cached_get_page("http://www.filmz.ru/film/%s/" % movie_id)
    soup = BeautifulSoup(page_content)
    film_info["title"] = get_title(soup)
    film_info["year"] = get_year(soup)
    film_info["description"] = get_description(soup)
    film_info["duration"] = get_duration(soup)
    film_info["genre"] = get_genre(soup)
    return film_info


if len(sys.argv) < 2 or not all(arg.isdigit() for arg in sys.argv[1:]):
    print "\nUSAGE: python get_title.py <film-id>+\n"
    sys.exit(1)

for id in sys.argv[1:]:
    print get_info(id)
