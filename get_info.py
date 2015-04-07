#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
import re
from bs4 import BeautifulSoup


def _get_title(soup):
    h1 = soup.h1
    # R: чтобы не писать цепочку if-ов можно пойти разными путями:
    #
    #       # Пишем как будто всё хорошо и ловим исключение, если это не так
    #       try:
    #           return h1.span.get_text()
    #       except AttributeError:
    #           return None
    #
    #       # Используем css-запрос
    #       span = soup.select('h1 > span:nth-of-type(1)')
    #
    # R: на самом деле, надо было использовать itemprop="name"
    if h1 != None:
        span = h1.span
        # R: с None сравниваем is None, а не на равенство
        if span != None:
            return span.get_text()
        # R: в питоне если функция дошла до конца и ничего не вернула, то она возвращает None.
        #    Так что эти можно опустить. Во многих случаях return None пишут всё равно,
        #    чтобы подчеркнуть намерение, но в данном случае лучше меньше мусора.
        return None
    return None


def _get_year(soup):
    # R: декларативный подход всегда лучше:
    #       year_span = soup.select('h1 > span:nth-of-type(2)')[0]
    h1 = soup.h1
    # R: if h1 is not None:
    if h1 != None:
        span = h1.find_all("span")
        if len(span) >= 2:
            # R: brackets - это квадратные скобки, круглые - parenthesses.
            #    Кроме того, название лишком специфичное, правильнее будет dirty_year,
            #    т.е. грязное, неочищенное значение.
            year_with_brackets = span[1].get_text()
            return int(year_with_brackets.strip("()"))
        # R: опять же return None можно не писать
        return None
    return None


def _get_description(soup):
    # R: проще использовать soup.find() и затем просто проверку, чем .findAll()/len(),
    #    также исчезнет неестественный доступ descriptions[0]
    descriptions = soup.findAll(itemprop="description")
    if len(descriptions) >= 1:
        return descriptions[0].get_text()
    return None


def _get_duration(soup):
    # R: опять же findAll() -> find()
    durations_with_text = soup.findAll(itemprop="runtime")
    if len(durations_with_text) > 0:
        duration_with_text = durations_with_text[0].get_text()
    else:
        # R: просто искать первый i на странице как-то слишком уж хрупко, фигня найдётся.
        #    Можно ограничить блоком каким-то.
        i = soup.i
        if i == None: # R: i is None
            return None
        else:
            duration_with_text = i.get_text()

    # R: квадратные скобки вокруг \D не нужны,
    # R: более эффективно заменять сразу несколько нецифр, а не по одной:
    #       re.sub(r'\D+', '', duration_with_text)
    # R: надёжнее сделать поиск с захватом:
    #
    #       m = re.search('\d+', duration_with_text)
    #       if m:
    #           return int(m.group())
    #
    #    т.к. сейчас строка 123,5 превратится в 1235,  два отдельных числа в строке могут
    #    соединится. В общем, возможны непотребства.
    # R: также можно получить исключение, если от строки ничего не останется.
    return int(re.sub(r'[\D]', '', duration_with_text))


def _get_genres(soup):
    # R: проще использовать soup.find() и затем просто проверку, чем .findAll()/len(),
    #    также исчезнет неестественный доступ genres[0]
    genres = soup.findAll(itemprop="genre")
    # R: можно просто if genres:
    if len(genres) >= 1:
        # R: genres_unsplitted - очень странное имя, оно содержит в себе то,
        #    что ты собираешься с этим делать - разделять.
        #    Более логичные варианты:
        #       - genres_string, genres_text
        #       - не использовать промежуточную переменнную:
        #           return genres[0].get_text().split(", ")
        genres_unsplitted = genres[0].get_text()
        return genres_unsplitted.split(", ")
    # R: некоторые считают, что лучше использовать ранний выход:
    #      genres = ...
    #      if not genres:
    #          return []
    #
    #      ... продолжаем
    return []


def get_info(movie_id):
    page_content = utils.cached_get_page("http://www.filmz.ru/film/%s/" % movie_id)
    soup = BeautifulSoup(page_content)
    return {
        'title' : _get_title(soup),
        'year' : _get_year(soup),
        'description' : _get_description(soup),
        'duration' : _get_duration(soup),
        'genres' :_get_genres(soup)
    }
