#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
import re
from bs4 import BeautifulSoup


def _get_title(soup):
    h1 = soup.h1
    span = h1.span
    return span.get_text()


def _get_year(soup):
    h1 = soup.h1
    span = h1.find_all("span")
    year_with_brackets = span[1].get_text()
    return int(year_with_brackets.strip("()"))


def _get_description(soup):
    descriptions = soup.findAll(itemprop="description")
    # доделать после проектирования API
    return descriptions[0].get_text()


def _get_duration(soup):
    durations_with_text = soup.findAll(itemprop="runtime")
    if len(durations_with_text) > 0:
        duration_with_text = durations_with_text[0].get_text() # после проектирования API доделать
    else:
        i = soup.i
        duration_with_text = i.get_text()
    return int(re.sub(r'[\D]', '', duration_with_text))


def _get_genre(soup):
    genres = soup.findAll(itemprop="genre")
    # доделать после проектирования API, если список будет пустой
    return genres[0].get_text()


def get_info(movie_id):
    page_content = utils.cached_get_page("http://www.filmz.ru/film/%s/" % movie_id)
    soup = BeautifulSoup(page_content)
    return {
        'title' : _get_title(soup),
        'year' : _get_year(soup),
        'description' : _get_description(soup),
        'duration' : _get_duration(soup),
        'genre' :_get_genre(soup)
    }

