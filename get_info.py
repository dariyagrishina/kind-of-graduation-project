#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
import re
from bs4 import BeautifulSoup


def _get_title(soup):
    h1 = soup.h1
    if h1 != None:
        span = h1.span
        if span != None:
            return span.get_text()
        return None
    return None


def _get_year(soup):
    h1 = soup.h1
    if h1 != None:
        span = h1.find_all("span")
        if len(span) >= 2:
            year_with_brackets = span[1].get_text()
            return int(year_with_brackets.strip("()"))
        return None
    return None


def _get_description(soup):
    descriptions = soup.findAll(itemprop="description")
    if len(descriptions) >= 1:
        return descriptions[0].get_text()
    return None


def _get_duration(soup):
    durations_with_text = soup.findAll(itemprop="runtime")
    if len(durations_with_text) > 0:
        duration_with_text = durations_with_text[0].get_text()
    else:
        i = soup.i
        if i == None:
            return None
        else:
            duration_with_text = i.get_text()

    return int(re.sub(r'[\D]', '', duration_with_text))


def _get_genres(soup):
    genres = soup.findAll(itemprop="genre")
    if len(genres) >= 1:
        genres_unsplitted = genres[0].get_text()
        return genres_unsplitted.split(", ")
    return []


def get_info(movie_id):
    page_content = utils.cached_get_page("http://www.filmz.ru/film/%s/" % movie_id)
    soup = BeautifulSoup(page_content)
    return {
        'title' : _get_title(soup),
        'year' : _get_year(soup),
        'description' : _get_description(soup),
        'duration' : _get_duration(soup),
        'genres' :_get_genres(soup)
    }
