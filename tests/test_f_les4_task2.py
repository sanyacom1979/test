import pytest

from f_les4_task2 import graf

# тест a != 0
def test_graf():
    with pytest.raises(Exception):
        graf(0, 1, 2, 10)