#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
from bs4 import BeautifulSoup


def get_title(film_number_list):
    film_names_list = []
    for film_number in film_number_list:
        page_content = utils.get_page("http://www.filmz.ru/film/%s/" % film_number)
        soup = BeautifulSoup(page_content)
        h1 = soup.h1
        span = h1.span
        text = span.get_text()
        film_names_list.append(text)
    return film_names_list


#agruments_list_length = len(sys.argv)
film_number_list = []
if len(sys.argv) < 2:
    print "\nUSAGE: python get_title.py <film-id>\n"
    sys.exit(1)
for index in range(1, len(sys.argv)):
    if not sys.argv[index].isdigit():
        print "\nUSAGE: python get_title.py <film-id>\n"
        sys.exit()
    else:
        film_number_list.append(sys.argv[index])

titles = get_title(film_number_list)
for title in titles:
    print title