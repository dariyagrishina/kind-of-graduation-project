# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
from cached_func import cached
from utils import get_page


def _get_title(soup):
    span = soup.find(itemprop="name")
    if span:
        return span.get_text()


def _get_year(soup):
    year_spans = soup.select('h1 > span:nth-of-type(2)')
    if year_spans:
        dirty_year = year_spans[0].get_text()
        return int(dirty_year.strip("()"))


def _get_description(soup):
    description = soup.find(itemprop="description")
    if description:
        return description.get_text()


def _get_duration(soup):
    element = soup.find(itemprop="runtime")
    if element:
        duration_with_text = element.get_text()
    else:
        # If runtime is not marked properly then we fallback to looking in tags
        elements = soup.select(".tags > i")
        if elements:
            duration_with_text = elements[0].get_text()
        else:
            return None

    m = re.search('\d+', duration_with_text)
    if m:
        return int(m.group())


def _get_genres(soup):
    genre = soup.find(itemprop="genre")
    if genre:
        return genre.get_text().split(", ")


@cached
def get_movies_info(movie_id):
    page_content = get_page("http://www.filmz.ru/film/%s/" % movie_id)
    soup = BeautifulSoup(page_content)
    return {
        'title': _get_title(soup),
        'year': _get_year(soup),
        'description': _get_description(soup),
        'duration': _get_duration(soup),
        'genres': _get_genres(soup)
    }
