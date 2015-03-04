#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import sys
import urllib


def get_page(url):
    page = urllib.urlopen(url)
    content = page.read()
    page.close()
    return content


#if len(sys.argv) < 2:
#    print "\nUSAGE: python get_page.py <page-url>\n"
#    sys.exit(1)
#else:
#    print get_page(sys.argv[1])


def get_title(film_number):
    page_content = get_page("http://www.kinopoisk.ru/film"+str(film_number)+"/")
    title_beginn = page_content.find("<title>")
    title_end = page_content.find("</title>", title_beginn)
    title = page_content[title_beginn + 7:title_end]
    return title

print get_title(401)
