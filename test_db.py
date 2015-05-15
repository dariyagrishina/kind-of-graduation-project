# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import db


MATRIX = {
    "title": "Матрица",
    "year": 1999,
    "description": "Хакер Томас Андерсон. Нео, должен стать их мессией. Экшн.",
    "genres": ["фантастика", "экшн"],
}


def test_movie_matches_item():
    # Test against each field
    assert db._movie_matches_item('матрица', MATRIX)
    assert db._movie_matches_item('нео', MATRIX)
    assert db._movie_matches_item('1999', MATRIX)
    assert db._movie_matches_item('фантастика', MATRIX)
    # Test mismatch
    assert not db._movie_matches_item('баловство', MATRIX)


def test_movie_matches():
    assert db._movie_matches('матрица', MATRIX)
    # Test search phrase parsing (mind coma after "Нео")
    assert db._movie_matches('Нео, должен', MATRIX)
    # Test against counting single term matching twice
    assert not db._movie_matches('экшн драма', MATRIX)
