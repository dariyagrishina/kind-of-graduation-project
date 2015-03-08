#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import sys
import urllib


def get_page(url):
    page = urllib.urlopen(url)
    content_cp1251 = page.read()
    content = content_cp1251.decode('cp1251')
    page.close()
    return content


if len(sys.argv) < 2:
    print "\nUSAGE: python get_page.py <page-url>\n"
    sys.exit(1)
else:
    print get_page(sys.argv[1])
