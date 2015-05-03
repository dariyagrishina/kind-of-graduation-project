# -*- coding: utf-8 -*-
import os
import json
from get_info import get_info


def save_data():
    hundred_films = []
    for movie_id in range(1, 101):
        movies_data = get_info(movie_id)
        hundred_films.append(movies_data)

    with open("100_movies_data.json", 'w') as f:
        f.write(json.dumps(hundred_films, ensure_ascii=False).encode('utf-8')) # ensure_ascii=False is used just to prove
                                                                               # that everything is OK


def load_data():
    with open("100_movies_data.json") as f:
        return json.load(f)
