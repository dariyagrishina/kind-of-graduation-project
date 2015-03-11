#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
from bs4 import BeautifulSoup


def get_title(film_number):
    page_content = utils.get_page("http://www.filmz.ru/film/%s/" % film_number)
    soup = BeautifulSoup(page_content)
    h1 = soup.h1
    span = h1.span
    text = span.get_text()
    return text


if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    print "\nUSAGE: python get_title.py <film-id>\n"
    sys.exit(1)
else:
    print get_title(sys.argv[1])
