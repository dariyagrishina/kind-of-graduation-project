# -*- coding: utf-8 -*-
import os
import json
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


def look_for_search_query(search_query):
    db = load_data()
    search_query_list = search_query.split()
    res = []
    for movie_info in db:
        search_status = 0
        for value in movie_info.values():
            for search_item in search_query_list:
                if search_item.isdigit():
                    if value is not None and int(search_item) == value:
                        search_status = search_status + 1
                else:
                    if value is not None and not isinstance(value, int) and search_item in value:
                        search_status = search_status + 1

        if search_status >= len(search_query_list):
            res.append(movie_info['title'])
    return res
