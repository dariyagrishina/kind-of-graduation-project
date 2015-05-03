# -*- coding: utf-8 -*-
import os
import json
from get_info import get_info


def _get_path(movie_id):
    current_path = os.path.dirname(__file__)
    data_path = os.path.join(current_path, "movies_data/" + str(movie_id))
    return data_path


def _save_info(movie_id, movies_data):
    with open(_get_path(movie_id), 'w') as f:
        f.write(json.dumps(movies_data, ensure_ascii=False).encode('utf-8')) # ensure_ascii=False is made just to prove
                                                                             # that everything is OK


def _load_info(movie_id):
    with open(_get_path(movie_id)) as f:
        return json.load(f)


def cached_get_info(movie_id):
    if os.path.isfile(_get_path(movie_id)):
        return _load_info(movie_id)
    else:
        movies_data = get_info(movie_id)
        _save_info(movie_id, movies_data)
        return movies_data
