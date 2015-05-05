# -*- coding: utf-8 -*-
import os
import json
from get_info import get_info


def save_data():
    movie_ids = range(1, 101)
    hundred_movies = map(get_info, movie_ids)

    with open("100_movies_data.json", 'w') as f:
        # ensure_ascii=False makes russian text human-readable
        f.write(json.dumps(hundred_movies, ensure_ascii=False).encode('utf-8'))


def load_data():
    with open("100_movies_data.json") as f:
        return json.load(f)
