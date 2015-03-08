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


def get_title(film_number):
    page_content = get_page("http://www.filmz.ru/film/%s/" % film_number)
    title_begin = page_content.find("<title>Filmz.ru")
    title_end = page_content.find("(", title_begin)
    title = page_content[title_begin + 17:title_end]
    return title


# R: аргументы коммандной строки всегда приходят как строки,
#    поэтому type(sys.argv[1]) == str всегда
# R: type(x) возвращает тип (класс), а не строку
#    поэтому стоит проверять type(var) is int (в данном случае там всё равно строка)
#    ещё лучше isinstance(var, int)
# R: правильно в данном случае было бы проверить, что в аргументе только цифры
#      var.isdigit()
if len(sys.argv) < 2 or type(sys.argv[1]) != "<type 'int'>":
    print "\nUSAGE: python get_title.py <film-id>\n"
    sys.exit(1)
else:
    print get_title(sys.argv[1])
