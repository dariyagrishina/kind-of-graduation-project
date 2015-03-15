#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils


if len(sys.argv) < 2:
    print "\nUSAGE: python get_page.py <page-url>\n"
    sys.exit(1)
elif:
    url = sys.argv[1]
    geloaded_content = load(url)
    if geloaded_content == None:
        save(url)
        print load(url)
    else:
        print geloaded_content

    #print utils.get_page(sys.argv[1])

def save(url):
    file_name = ""
    for character in url:
        file_name = file_name + _ + ord(character)
    content = utils.get_page(sys.argv[1])


def load(url):

    # ...
    return content
