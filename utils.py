# -*- coding: utf-8 -*-
import urllib
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


def save(url, content):
    file_name = get_file_name(url)
    cached_page = open("cached_pages/" + get_file_name(url), "w")
    cached_page.write(content.encode('utf8'))
    cached_page.close()


def load(url):
    file_name = get_file_name(url)
    cached_page = open("cached_pages/" + get_file_name(url), "r")
    content = cached_page.read()
    cached_page.close()
    return content.decode("utf8")


def cached_get_page(url):
    if os.path.isfile(get_file_name(url)):
        return load(url)
    else:
        content = get_page(url)
        save(url, content)
        return content
