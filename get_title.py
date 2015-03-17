#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
from bs4 import BeautifulSoup


def get_title(movie_id):
    page_content = utils.cached_get_page("http://www.filmz.ru/film/%s/" % movie_id)
    soup = BeautifulSoup(page_content)
    h1 = soup.h1
    span = h1.span
    return span.get_text()


if len(sys.argv) < 2 or not all(arg.isdigit() for arg in sys.argv[1:]):
    print "\nUSAGE: python get_title.py <film-id>+\n"
    sys.exit(1)

for id in sys.argv[1:]:
    print get_title(id)
