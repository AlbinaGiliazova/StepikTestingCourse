# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:36:57 2021
Задание: пропуск тестов
Изучите самостоятельно документацию про маркировку xfail. Найдите там параметр, который в случае неожиданного прохождения теста, помеченного как xfail, отметит в отчете этот тест как упавший. Пометьте таким образом первый тест из этого тестового набора.
https://docs.pytest.org/en/latest/reference/reference.html?highlight=xfail#pytest.mark.xfail

test_xfail.py:

import pytest


def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
Запустите полученные тесты. Обратите внимание на статус прогона тестов. Найдите последнюю строчку с итогами запуска, скопируйте текст между символами === и отправьте его в качестве ответа на это задание. 
@author: gilia
"""
import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
