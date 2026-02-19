import pytest
from src.calculator import add, divide, subtract, multiply


def test_add_valid():
    assert add(2, 3) == 5


def test_subtract_valid():
    assert subtract(5, 2) == 3


def test_multiply_valid():
    assert multiply(3, 4) == 12


def test_divide_valid():
    assert divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_add_negative():
    assert add(-1, -1) == -2


def test_subtract_negative():
    with pytest.raises(ValueError):
        subtract(-1, 1)

    with pytest.raises(ValueError):
        subtract(1, -1)


def test_multiply_negative():
    assert multiply(-2, 3) == -6
