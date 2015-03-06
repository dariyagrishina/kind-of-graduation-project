#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import sys
import urllib


# R: стандартная практика - функции внутри программы работают с логическими строками,
#    и преобразование происходит при вводе и выводе.
#    т.е. get_title() как внутренняя функция вообще ничего не должна знать о кодировках.
#
#    План такой:
#       - get_page() получает бинарную строку из page.read() и тут же её декодирует,
#       - get_title() получает страницу в декодированном виде и выдаёт название фильма,
#         также в декодированном виде,
#       - код вызывающий get_title() ответственен за кодирование результата если хочет его вывести.
#
#    Это хорошо потому что
#       - с таким get_page() легче работать,
#       - результат get_title() может и не пойти на консоль, а подвергнутся дальнейшей обработке.


def get_page(url):
    page = urllib.urlopen(url)
    content = page.read()
    page.close()
    return content


def get_title(film_number):
    # R: используй форматирование строк вместо конкатенации -
    #    http://pythonworld.ru/osnovy/formatirovanie-strok-operator.html
    page_content = get_page("http://www.kinopoisk.ru/film" + str(film_number) + "/")

    # R: title_beginn -> title_begin
    title_beginn = page_content.find("<title>")
    title_end = page_content.find("</title>", title_beginn)
    # R: лучше не использовать одно и то же имя для разных вещей
    #    title_cp1251 = page_content[...]
    #    title = title_1251.decode(...)
    #    title_utf8 = title.encode(...)
    title = page_content[title_beginn + 7:title_end]
    title = title.decode('cp1251')
    title = title.encode("utf8")
    return title # получился, на самом деле, совсем не фильм, но ввиду блокировки не могу дальше практиковаться



if len(sys.argv) < 2:
    print "\nUSAGE: python get_page.py <page-url>\n"
    sys.exit(1)
else:
    print get_title(sys.argv[1])
