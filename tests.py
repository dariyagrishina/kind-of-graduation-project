# -*- coding: utf-8 -*-
import get_info


def test_get_info():
    matrix = get_info.get_info(13)

    assert matrix['title'] == u'Матрица'
    assert matrix['year'] == 1999

    assert 750 <= len(matrix['description']) <= 850
    assert matrix['description'][:30] == u'В один далеко не прекрасный де'

    assert matrix['duration'] == 136
    assert matrix['genres'] == [u'фантастика', u'экшн']


def test_get_info_exceptions():
    matrix = get_info.get_info(124)

    assert matrix['title'] == u'Ледяная внучка'
    assert matrix['year'] == 1981

    assert 150 <= len(matrix['description']) <= 250
    assert matrix['description'][:30] == u'Сказка о Снегурочке, внучке Де'

    assert matrix['duration'] == None
    assert matrix['genres'] == [u'сказка', u'фэнтези', u'семейный']

