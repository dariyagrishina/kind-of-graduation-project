# -*- coding: utf-8 -*-
import os
import json
import re
from get_info import get_movies_info


def save_data():
    movie_ids = range(1, 101)
    hundred_movies = map(get_movies_info, movie_ids)

    with open("100_movies_data.json", 'w') as f:
        # ensure_ascii=False makes russian text human-readable
        f.write(json.dumps(hundred_movies, ensure_ascii=False).encode('utf-8'))


def load_data():
    with open("100_movies_data.json") as f:
        return json.load(f)

# R: для описания того, что функция делает использут docstring
# convert unicode text to lowercase list without punctuation marks
# R: название вводит в заблуждение двумя способами
#    - modify предполагает, что переданный аргумент будет изменён,
#    - modify предполагает, что у нас останется текст, но мы внезапно возвращаем список.
#
#    нужно решить как ты назовёшь полученные штуки (слова, термы, токены)
#    и назвать функцию соответствующе.
#
#    Также процесс разбора называется парсингом, тогда вызов может выглядеть как:
#       tokens = _parse(text)
def _modify_text(text):
    text_lowercase = text.lower()
    # R: text_list - список текстов
    text_list = re.findall('\w+', text_lowercase, flags=re.U)
    return text_list

# R: главно всё же, что мы матчим (фильмы), поэтому это должно быть в названии.
#    А search и match имеют перекрывающиеся значения, поэтому тут тавтология.
#    Можно назвать, например, _movie_matches_item().
def _search_item_matches(search_item, movie_info):
    # R: слишком длинная строка
    # R: str(movie_info["year"]) or "" - ошибка, т.к. str(None) or "" == 'None'
    text = (movie_info["description"] or "") + " " + (movie_info["title"] or "") + " " + (str(movie_info["year"]) or "")
    if movie_info['genres'] is not None:
        # R: неэффективный способ конкатенации строк, да и хлопотный, нужно использовать join
        for e in movie_info["genres"]:
            text = text + " " + e
    # R: т.к. мы всё равно получаем массив, то можно было его растить постепенно:
    #       tokens = []
    #       tokens.extend(_parse(movie_info['description'] or ''))
    #       if movie_info['year']:
    #           tokens.extend(_parse(str(movie_info['year'])))
    #       ...
    # R: modified_text - неправильное имя, т.к. это не текст, а список
    modified_text = _modify_text(text)

    # R: это то же самое что
    #       return search_item in modified_text
    if search_item in modified_text:
        return True
    return False


def _movie_matches(search_query, movie_info):
    # R: modified_search_query - слишком мутное имя, которое никак не намекает,
    #    что у нас теперь там список слов. Можно назвать:
    #       - search_items
    #       - search_words
    #       - search_tokens
    #       - search_terms
    modified_search_query = _modify_text(search_query)
    # R: смысл запрос матчит если все его слова (термы, токены) матчат в питоне отлично выражается
    #    функцией all():
    #       return all(_search_item_matches(item, movie_info) for item in search_items)
    for search_item in modified_search_query:
        if not _search_item_matches(search_item, movie_info):
            return False
    return True


# R: мы ищем фильмы, а не поисковый запрос
# R: look for - подискивать, приглядывать. В такой ситуации как здесь традиционно используеться
#    search или find.
def look_for_search_query(search_query):
    db = load_data()
    # R: т.к. это не функция ввода-вывода, то она не должна заниматься перекодировкой,
    #    она должна уже работать с юникодом
    search_query_unicode = search_query.decode('utf-8')
    return [movie_info['title'] for movie_info in db
                                if _movie_matches(search_query_unicode, movie_info)]
