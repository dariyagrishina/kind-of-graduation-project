# -*- coding: utf-8 -*-
import get_info


def test_get_info():
    matrix = get_info.get_info(13)

    assert matrix['title'] == u'Матрица'
    assert matrix['year'] == 1999
    assert matrix['description'] == u'В один далеко не прекрасный день хакер Томас Андерсон начинает ощущать на себе пристальное внимание таинственных незнакомцев, которые то пытаются передать ему какую-то важную информацию, то, наоборот, преследуют его и стараются убить. Спасшись от погони, Томас обнаруживает, что действительность девяностых годов — не более, чем виртуальная подделка. На самом деле время ушло далеко вперед, и люди, которые думают, что живут, любят и работают, в реальности погружены в глубокий летаргический сон и содержатся в специальных контейнерах, служа источниками жизненной энергии для таинственных электронных монстров. Горстка бодрствующих отщепенцев во главе с невозмутимым гуру Морфеем пытается разрушить  зловещий мирок. И Андерсон, который в настоящем мире носит имя Нео, должен стать их мессией.'
    assert matrix['duration'] == 136
    assert matrix['genres'] == [u'фантастика', u'экшн']

test_get_info()
