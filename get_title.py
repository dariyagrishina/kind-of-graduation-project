#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
from bs4 import BeautifulSoup # R: далее должно идти 2 пустых строки, не 3



def get_title(film_number):
    page_content = utils.get_page("http://www.filmz.ru/film/%s/" % film_number)
    soup = BeautifulSoup(page_content)
    # R: это строчка не нужна
    soup.prettify()
    # R: почему h1_line и span_line? в данном случае это объект BeautifulSoup,
    #    который отвечает за html-тег. Поэтому h1_tag или просто h1.
    h1_line = soup.h1
    span_line = h1_line.span
    text = span_line.get_text()
    return text


if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    print "\nUSAGE: python get_title.py <film-id>\n"
    sys.exit(1)
else:
    print get_title(sys.argv[1])
