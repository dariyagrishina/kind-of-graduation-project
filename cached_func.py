# -*- coding: utf-8 -*-
import os
import json
from utils import get_page
from get_info import get_movies_info


def _get_path(movie_id):
    current_path = os.path.dirname(__file__)
    data_path = os.path.join(current_path, "movies_data/" + str(movie_id))
    return data_path


def _save_info(movie_id, movies_data):
    with open(_get_path(movie_id), 'w') as f:
        f.write(json.dumps(movies_data, ensure_ascii=False).encode('utf-8'))


def _load_info(movie_id):
    with open(_get_path(movie_id)) as f:
        return json.load(f)


def cached_get_info(movie_id):
    if os.path.isfile(_get_path(movie_id)):
        return _load_info(movie_id)
    else:
        movies_data = get_movies_info(movie_id)
        _save_info(movie_id, movies_data)
        return movies_data

# cached(func) begin

def _get_file_name(arg):
    return '_'.join(str(ord(c)) for c in str(arg))


def _get_folder_name(func):
    folder_name_dirty = str(func)
    point = folder_name_dirty.find("at")
    folder_name = folder_name_dirty[1:point-1]
    return "/".join(("cache", folder_name))


def _get_path_file(arg, func):
    return _get_path_folder(func) + "/" + _get_file_name(arg)


def _get_path_folder(func):
    current_path = os.path.dirname(__file__)
    folder_path = os. path.join(current_path, _get_folder_name(func))
    return folder_path


def _save(arg, data, func):
    if not os.path.exists(_get_path_folder(func)):
        os.mkdir(_get_path_folder(func))
    with open(_get_path_file(arg, func), 'w') as f:
        f.write(json.dumps(data))


def _load(arg, func):
    with open(_get_path_file(arg, func)) as f:
        return json.load(f)


def cached(func):
    def cached_func(arg):
        if os.path.isfile(_get_path_file(arg, func)):
            return _load(arg, func)
        else:
            data = func(arg)
            _save(arg, data, func)
            return data
    return cached_func
