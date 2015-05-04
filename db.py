# -*- coding: utf-8 -*-
import os
import json
from get_info import get_info


def save_data():
    hundred_films = map(get_info, range (1,))
    with open("100_movies_data.json", 'w') as f:
        # R: ensure_ascii=False makes russian text humanreadable
        f.write(json.dumps(hundred_films, ensure_ascii=False).encode('utf-8'))


def load_data():
    with open("100_movies_data.json") as f:
        return json.load(f)
