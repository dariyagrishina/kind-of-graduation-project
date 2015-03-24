#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
from bs4 import BeautifulSoup


# R: функции get_title(), get_year(), ... типа служебные в питоне их принято называть с _:
#
#       def _get_title(soup):
#           ...
#
#    альтернативный вариант - положить их в get_info():
#
#       def get_info(...):
#           def get_title(...):
#               ...
#
#           def get_year(...):
#               ...
#
#           description = lambda soup: soup.p.get_text()
#
#           ...
#
#    тогда снаружи они будут не видны.

def get_title(soup):
    h1 = soup.h1
    span = h1.span
    return span.get_text()


def get_year(soup):
    h1 = soup.h1
    span = h1.find_all("span")
    year_with_brackets = span[1].get_text()
    return year_with_brackets.strip("()")


def get_description(soup):
    # R: это очень, очень, очень, просто невероятно ненадёжный способ доставать данные.
    #    тег <p> - это просто параграф, что угодно на странице может быть в параграфе.
    p = soup.p
    return p.get_text()


def get_duration(soup):
    # R: тоже очень, очень, ну ты поняла, ненадёжный способ
    #    не работает, например для матрицы (id = 13).
    i = soup.i
    duration_with_text = i.get_text()
    # R: когда хочешь что-то отфильтровать следует использовать filter:
    #
    #       duration = ''.join(filter(unicode.isdigit(), duration_with_text))
    #
    #    или генераторные выражения:
    #
    #       duration = ''.join(c for c in duration_with_text if c.isdigit())
    #
    #    Но в случае поиска подстроки по шаблону лучше всего подходят регулярные выражения.
    #    Узнай о них. По английски это regular expressions.
    duration = ""
    for character in duration_with_text:
        if character.isdigit():
            duration += character
    return duration


def get_genre(soup):
    # R: нехорошо называть список в единственном числе
    genre = soup.findAll(itemprop="genre")
    # R: а если не найдет? список будет пустой и genre[0] вызовет ошибку
    return genre[0].get_text()


def get_info(movie_id):
    # R: создали словарь здесь, а используем потом, лучше не распылять
    film_info = {}
    page_content = utils.cached_get_page("http://www.filmz.ru/film/%s/" % movie_id)
    soup = BeautifulSoup(page_content)
    # R: логические куски код принято разделять пустыми строками, даже внутри функции
    #    тут можно, например, отделить парсинг, который идёт ниже.
    #    Вообще если у тебя больше 4-5 строк кода подряд, то у тебя должна быть хорошая причина,
    #    почему они не отделены.
    # R: можно использовать литерал словаря, чтобы не повторять film_info:
    #
    #       return {
    #           'title': get_title(soup),
    #           ...
    #       }
    film_info["title"] = get_title(soup)
    film_info["year"] = get_year(soup)
    film_info["description"] = get_description(soup)
    film_info["duration"] = get_duration(soup)
    film_info["genre"] = get_genre(soup)
    return film_info


if len(sys.argv) < 2 or not all(arg.isdigit() for arg in sys.argv[1:]):
    # R: не соответствует
    print "\nUSAGE: python get_title.py <film-id>+\n"
    sys.exit(1)

for id in sys.argv[1:]:
    print get_info(id)
