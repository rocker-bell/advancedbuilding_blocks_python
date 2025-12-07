import pytest
from src.pyblocks.enumerables import Enumerable as E

def test_my_select():
    arr = [1, 2, 3, 4]
    assert E.my_select(arr, lambda x: x % 2 == 0) == [2, 4]

def test_my_all():
    arr = [2, 4, 6]
    assert E.my_all(arr, lambda x: x % 2 == 0) is True

def test_my_inject_sum():
    arr = [1, 2, 3, 4]
    result = E.my_inject(arr, 0, '+')
    assert result == 10
