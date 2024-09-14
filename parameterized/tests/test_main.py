import pytest 
from src.main import add, is_palindrome


@pytest.mark.parametrize( "a, b, expected",
    [
        (5, 5, 10),
        (5, -4, 1),
        (0, 0, 0),
        (-5, -5, -10)
    ],)
def test_add(a, b, expected):
    assert add(a,b) == expected

@pytest.mark.parametrize( "s, expected",
    [
        ('car', False),
        ('cac', True),
        ('amanaplanacanalpanama', True),
        ('raceacar', False),
    ],)
def test_is_palindrom(s, expected):
    assert is_palindrome(s) == expected
