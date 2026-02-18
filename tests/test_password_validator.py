import pytest
from src.password_validator import validate_password


def test_valid_password():
    assert validate_password("StrongPass1@") is True


def test_too_short():
    assert validate_password("S1a") is False


def test_no_uppercase():
    assert validate_password("weakpass1") is False


def test_no_digit():
    assert validate_password("WeakPassword") is False


def test_contains_space():
    assert validate_password("Weak Pass1") is False


def test_empty_string():
    assert validate_password("") is False


def test_non_string_input():
    assert validate_password(12345) is False

def test_no_special_character():
    assert validate_password("WeakPass1") is False