import pytest
from src.calculator import add, divide


def test_add_valid():
    assert add(2, 3) == 5


def test_divide_valid():
    assert divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_add_negative():
    assert add(-1, -1) == -2
