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

# convert unicode text to lowercase list without punctuation marks
def _modify_text(text):
    text_lowercase = text.lower()
    text_list = re.findall('\w+', text_lowercase, flags=re.U)
    return text_list

def _search_item_matches(search_item, movie_info):
    text = (movie_info["description"] or "") + " " + (movie_info["title"] or "") + " " + (str(movie_info["year"]) or "")
    if movie_info['genres'] is not None:
        for e in movie_info["genres"]:
            text = text + " " + e
    modified_text = _modify_text(text)

    if search_item in modified_text:
        return True
    return False


def _movie_matches(search_query, movie_info):
    modified_search_query = _modify_text(search_query)
    for search_item in modified_search_query:
        if not _search_item_matches(search_item, movie_info):
            return False
    return True


def look_for_search_query(search_query):
    db = load_data()
    search_query_unicode = search_query.decode('utf-8')
    return [movie_info['title'] for movie_info in db
                                if _movie_matches(search_query_unicode, movie_info)]
