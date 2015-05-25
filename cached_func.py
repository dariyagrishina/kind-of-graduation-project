# -*- coding: utf-8 -*-
import os
import json


def _get_file_name(arg):
    return '_'.join(str(ord(c)) for c in str(arg))


def _get_folder_name(func):
    # R: есть куда более простой способ получить имя функции:
    #        func.__name__
    #    кроме того, у тебя в пути остаётся пробел, что работает, но потенциально несёт проблемы.
    folder_name_dirty = str(func)
    point = folder_name_dirty.find("at")
    folder_name = folder_name_dirty[1:point-1]
    return "/".join(("cache", folder_name))


# R: нелогичный порядок аргументов. Это же функция и её аргумент,
#    а не аргумент со своей функцией.
def _get_path_file(arg, func):
    return _get_path_folder(func) + "/" + _get_file_name(arg)


def _get_path_folder(func):
    # R: это константа, её следует посчитать один раз
    current_path = os.path.dirname(__file__)
    # R: пробел лишний после os.
    folder_path = os. path.join(current_path, _get_folder_name(func))
    return folder_path


# R: нелогичный порядок аргументов. Данные должны идти в конце,
#    т.к. остальные аргументы определяют, что с ними делать.
#    Взаимосвязанные аргументы func и arg разбросаны хаосом.
def _save(arg, data, func):
    # R: _get_path_folder() дважды считает одно и то же
    if not os.path.exists(_get_path_folder(func)):
        os.mkdir(_get_path_folder(func))
    # R: _get_path_file() вызывает _get_path_folder() с теми же аргументами ещё раз.
    with open(_get_path_file(arg, func), 'w') as f:
        f.write(json.dumps(data))


# R: нелогичный порядок аргументов.
def _load(arg, func):
    with open(_get_path_file(arg, func)) as f:
        return json.load(f)


def cached(func):
    def cached_func(arg):
        # R: имя файла и папки вычисляется незнамо сколько раз.
        #    Стандартный подход в кеширвании - вычисляем имя файла в самом начале,
        #    позже оперируем только им, а не передаём везде функцию и аргумент.
        #
        #    Что если аргментов станет два? Тебе придётся всё переписать,
        #    а если имя файла вычисляется один раз, то поправить будет элементарно.
        if os.path.isfile(_get_path_file(arg, func)):
            return _load(arg, func)
        else:
            data = func(arg)
            _save(arg, data, func)
            return data
    return cached_func
