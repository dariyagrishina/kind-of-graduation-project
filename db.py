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


def _parse(text):
    """convert unicode text to lowercase list without punctuation marks."""
    text_lowercase = text.lower()
    tokens = re.findall('\w+', text_lowercase, flags=re.U)
    return tokens


def _movie_matches_item(search_item, movie_info):
    tokens = []
    if movie_info['year']:
        tokens.extend(_parse(str(movie_info['year'])))
    tokens.extend(_parse(movie_info['description'] or ''))
    tokens.extend(_parse(movie_info["title"] or ''))
    if movie_info["genres"]:
        for genre in movie_info["genres"]:
            tokens.extend(_parse(genre))

    return search_item in tokens


def _movie_matches(search_query, movie_info):
    search_items = _parse(search_query)
    return all(_movie_matches_item(item, movie_info) for item in search_items)


def movie_search(search_query):
    db = load_data()
    return [movie_info for movie_info in db
                       if _movie_matches(search_query, movie_info)]


def human_readable(data):
    return json.dumps(data, ensure_ascii=False).encode('utf-8')
