#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import sys
import urllib
import mymodule


def get_title(film_number):
    page_content = mymodule.get_page("http://www.filmz.ru/film/%s/" % film_number)
    title_begin = page_content.find("<title>Filmz.ru")
    title_end = page_content.find("(", title_begin)
    title = page_content[title_begin + 17:title_end]
    return title


if len(sys.argv) < 2 or not sys.argv[1].isdigit():
    print "\nUSAGE: python get_title.py <film-id>\n"
    sys.exit(1)
else:
    print get_title(sys.argv[1])
