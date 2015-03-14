#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
from bs4 import BeautifulSoup


# R: функция была изуродована, вместо того, чтобы ломать работающую функцию,
#    нужно было написать новую, которая бы вызывала старую.
#    Название get_title намекает на то, что что-то пошло не так,
#    она же теперь возвращает список названий, а не одно.
def get_title(film_number_list):
    # R: _list излишне, достаточно признака множественного числа:
    #       film_number_list -> film_numbers
    #       film_names_list -> film_names
    # R: на самом деле, это не номера фильмов, а идентификаторы:
    #       film_numbers -> film_ids
    # R: по английски фильм - movie:
    #       film_ids -> movie_ids
    #       film_names -> movie_names
    film_names_list = []
    for film_number in film_number_list:
        page_content = utils.get_page("http://www.filmz.ru/film/%s/" % film_number)
        soup = BeautifulSoup(page_content)
        h1 = soup.h1
        span = h1.span
        text = span.get_text()
        film_names_list.append(text)
    return film_names_list


# R: мертвечина
#agruments_list_length = len(sys.argv)
film_number_list = []
if len(sys.argv) < 2:
    # R: сообщение об использовании устарело, т.к. теперь можно передавать несколько id.
    #    Такую ситуацию обычно обозначают:
    #       USAGE: python get_title.py <film-id>+
    #    "+" означает повторить 1 или более раз
    print "\nUSAGE: python get_title.py <film-id>\n"
    sys.exit(1)
# R: можно сделать срез аргументов и идти по нему, индексы не нужны:
#       for arg in sys.argv[1:]:
#           if not arg.isdigit():
#               ...
for index in range(1, len(sys.argv)):
    if not sys.argv[index].isdigit():
        # R: дублируем ту же строку, нужно сделать одно из двух:
        #     - вынести строку в именованную константу,
        #     - преобразовать код так, чтобы использования строки совместились.
        print "\nUSAGE: python get_title.py <film-id>\n"
        sys.exit() # R: sys.exit(1), т.к. это ошибка
    else:
        # R: мы делаем работу даже если потом встретим косячный аргумент, нехорошо
        film_number_list.append(sys.argv[index])

titles = get_title(film_number_list)
for title in titles:
    print title
