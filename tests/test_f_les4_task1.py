import pytest

from math import sqrt

from f_les4_task1 import s_plit, korny


# тест a != 0
def test_korny1():
    with pytest.raises(Exception):
        korny(0, 1, 2)


# тест при дискриминанте > 0
def test_korny2():
    assert korny(1, 3, 1) == ((-3 + sqrt(5)) / 2, (-3 - sqrt(5)) / 2)


# тест при дискриминанте = 0
def test_korny3():
    assert korny(1, 2, 1) == -1

# тест при дискриминанте < 0


def test_korny4():
    assert korny(2, 2, 1) == "Нет корней"

# тест на количество аргументов


def test_korny5():
    with pytest.raises(Exception):
        korny(0, 1, 2, 3)


