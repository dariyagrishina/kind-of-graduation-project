# -*- coding: utf-8 -*-
import urllib
import os
import os.path


def get_page(url):
    page = urllib.urlopen(url)
    # TODO: detect encoding
    content_cp1251 = page.read()
    content = content_cp1251.decode('cp1251')
    page.close()
    return content


def get_file_name(url):
    return '_'.join(str(ord(c)) for c in url)


def page_path(url):
    current_path = os.path.dirname(__file__)
    page_path = os.path.join(current_path, "cached_pages/" + get_file_name(url))
    return page_path


def save(url, content):
    cached_page_file = open(page_path(url), "w")
    cached_page_file.write(content.encode('utf8'))
    cached_page_file.close()


def load(url):
    cached_page_file = open(page_path(url), "r")
    content = cached_page_file.read()
    cached_page_file.close()
    return content.decode("utf8")


def cached_get_page(url):
    if os.path.isfile(page_path(url)):
        return load(url)
    else:
        content = get_page(url)
        save(url, content)
        return content
